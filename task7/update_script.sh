#!/bin/bash
ssh -i /home/ubuntu/.ssh/task7.pem ubuntu@10.0.1.250 'sudo apt update -y && echo "Update was "$(date) >> script_run_log.log'
