import boto3
import paramiko
import time
import pprint
import subprocess

key = 'task2'


def connecttohost(host, username, key):
    host = host           # Public IP Address
    username = username   # default user for ubuntu
    key = key + '.pem'    # ssh key
    pkey = paramiko.RSAKey.from_private_key_file(key) 
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(host, username=username, pkey=pkey)               # connect to ec2 instance
    return client


def installaws(script, client):
    with open(script, "r") as f:
        sc = f.read()
    stdin, _stdout, _stderr = \
        client.exec_command(f" echo '{sc}'  > ~/installaws.sh")                # write .sh script to instance
    _stdin, _stdout, _stderr = \
        client.exec_command("sudo chmod +x ./installaws.sh && ./installaws.sh")   # execute .sh script
   
    time.sleep(10)

    with open('config', "r") as f:
        config = f.read()
    _stdin, _stdout, _stderr = \
        client.exec_command(f" echo '{config}'  > ~/.aws/config")              # write config file for aws cli
    print("config written")
    with open('credentials', "r") as f:
        credentials = f.read()
    _stdin, _stdout, _stderr = \
        client.exec_command(f" echo '{credentials}'  > ~/.aws/credentials")     # write file with Access-keys for aws cli
    print('credentials written')
    del client, _stdin, _stdout, _stderr


ec2 = boto3.client('ec2')
response = ec2.describe_instances()
data = response['Reservations']
version_and_host = []
for d in data:
    if d['Instances'][0]['State']['Code'] == 16:    # Check that instance running
        version = d['Instances'][0]['PlatformDetails']
        host = d['Instances'][0]['PublicIpAddress']    # get PublicIpAddress, Image-Id, OS name 
        image = d['Instances'][0]['ImageId']
        res = ec2.describe_images(ImageIds=[image,],)
        os_name = res['Images'][0]['Name']
        architec = res['Images'][0]['Architecture']
        info = {'version': version,
                'host': host,
                'os_name': os_name,
                'architec': architec}
        version_and_host.append(info)


for v in version_and_host:                 # Accoring OS execute .sh or .ps1 script for installing aws cli
    pprint.pprint(v)
    if 'ubuntu' in v['os_name']:
        print('UBUNTU')
        host = v['host']
        username = "ubuntu"
        key = 'task2'
        client = connecttohost(host, username, key)
        script = 'deb_ubuntu.sh'
        installaws(script, client)
 
    if 'debian' in v['os_name']:
        print('debian')
        host = v['host']
        username = "admin"
        key = 'task2'
        client = connecttohost(host, username, key)
        script = 'deb_ubuntu.sh'
        installaws(script, client)
    if 'RHEL' in v['os_name'] or 'CentOS' in v['os_name']:
        print('RED hat or CentOS')
        host = v['host']
        username = "ec2-user"
        key = 'task2'
        client = connecttohost(host, username, key)
        script = 'redhat.sh'
        installaws(script, client)
    if 'macOS' in v['os_name']:
        print('macOS')
        host = v['host']
        username = "ec2-user"
        key = 'task2'
        client = connecttohost(host, username, key)
        script = 'macOS.sh'
        installaws(script, client)
    if 'Windows' in v['os_name']:
        print('Windows')
        host = v['host']
        username = "Administrator"
        key = 'task2'
        subprocess.run(('/home/starik/Documents/tasks/trainee4/scripts/win.sh'), shell=True)