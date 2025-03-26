
#!/bin/bash
sshpass -f "pass" scp ./power.ps1  Administrator@44.203.252.97:/C:/Users/Administrator
sshpass -f "pass" ssh   Administrator@44.203.252.97 "powershell.exe .\power.ps1"