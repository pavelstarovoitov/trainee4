#!/bin/bash
sudo apt update -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip -y
#sudo yum install unzip -y
unzip awscliv2.zip
sudo ./aws/install
mkdir .aws