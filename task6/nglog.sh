#!/bin/bash

LOGFILE=/var/log/nginx/access.log # Path to nginx log file
let SIZELIMIT=90000  # size limit for temp log file
let CURSIZE=$(wc -c $LOGFILE | awk '{print $1}')
LOGFOLDER=/var/www/logs

if [ $CURSIZE -lt $SIZELIMIT ] 
then
    let ntail=$(wc -l $LOGFILE | awk '{print $1}') #if log file small get all lines
else
    let ntail=10  # else get last 100 lines
fi

 
while [ true ]      # infinity loop
do  
    
    currentline=$(wc -l $LOGFILE | awk '{print $1}') #get current line in log file
    tail -n $ntail $LOGFILE >> $LOGFOLDER/temp.log  #get lines added in period of 5 second

    size=$(wc -c $LOGFOLDER/temp.log | awk '{print $1}')  # check size

    if [ $size -gt $SIZELIMIT ]
    then
        cat /dev/null > $LOGFOLDER/temp.log            # if size of temp file too big, then flash file
        date=$(date)                                             # get current time and date
        echo "temp.log flashed -- $date"   >> $LOGFOLDER/flash.log   # create record about flashing file 
    else
        echo "less"                        # if size OK, do nothing
    fi   

    if [ $ntail -gt 0 ]      # if temp log has new lines, then check if that line include 4** of 5** errors           
    then
        tail -n $ntail $LOGFOLDER/temp.log |  awk '($9 ~ /4[0-5][0-9]/)' >> $LOGFOLDER/400.log  
        tail -n $ntail $LOGFOLDER/temp.log |  awk '($9 ~ /5[0-1][0-9]/)' >> $LOGFOLDER/500.log
    fi

    sleep 5                 # wait 5 second 

    linebecame=$(wc -l $LOGFILE | awk '{print $1}')  # check if access.log has new lines
    let ntail=$linebecame-$currentline              # check if access.log has new lines

done