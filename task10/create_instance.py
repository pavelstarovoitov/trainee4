# This script create one instance in EC2 using boto3 than
# get information about instance usunig paramiko,
# change ssh public key on instance and than terminate instance
import boto3
import paramiko
import pprint
import time


securitygroup_group_id = 'sg-00bdfd2e368c13bd8'   # security group that have security rule for ssh port 22
subnet_id = 'subnet-0e89c550b9ad8a6e3'
key = 'task2'                                     # key that will be used by paramiko
name = 'myname'                                   # custom name for instance
localkey = "task10.pub"                           # public key that will replace key on instance


def createinstance(securitygroup_group_id, subnet_id, key, name):  # create one t2.micro instance  with ubuntu and name 'myname'
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId="ami-084568db4383264d4",
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        NetworkInterfaces=[{
            'SubnetId': subnet_id,
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': True,
            'Groups': [securitygroup_group_id]
        }],
        TagSpecifications=[{
                    'ResourceType': 'instance',
                    'Tags': [{
                        'Key': 'Name',
                        'Value': name
                    },]
        },],
        KeyName=key)
    return (instance)


def terminateinstance(InstanceIds):  # terminate instance using InstanceIds as key to find instance 
    if isinstance(InstanceIds, str):
        ins = []
        ins.append(InstanceIds)
        InstanceIds = ins          # ec2.instances.filter work with list, so  InstanceIds must be transformed from str to list
    print(InstanceIds)
    ec2 = boto3.resource('ec2')
    response = ec2.instances.filter(InstanceIds=InstanceIds).terminate()  # terminate instance
    print("instance deleted: ", InstanceIds)
    return (response)


instance = createinstance(securitygroup_group_id, subnet_id, key, name)  # call fuction that create instance and return
print(instance[0])                                                       # InstanceIds class 
instance = instance[0].id                                                # get InstanceIds string from InstanceIds class
print(instance)
time.sleep(30)

ec2 = boto3.client('ec2')
response = ec2.describe_instances(InstanceIds=[instance,],)            
host = response['Reservations'][0]['Instances'][0]['PublicIpAddress']   # get Public IP Address for created instance
pprint.pprint(host)


def getmetrics(host, key):
    host = host          #  Public IP Address
    username = "ubuntu"  # default user for ubuntu
    key = key + '.pem'   # ssh key
    pkey = paramiko.RSAKey.from_private_key_file(key) 
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(host, username=username, pkey=pkey)
    _stdin, _stdout, _stderr = client.exec_command("df -h")    # get info about disks
    print(_stdout.read().decode())
    _stdin, _stdout, _stderr = client.exec_command("free -m")  # get info about RAM
    print(_stdout.read().decode()) 
    _stdin, _stdout, _stderr = client.exec_command("ip a")     # get info about network interfaces
    print(_stdout.read().decode())
    _stdin, _stdout, _stderr = client.exec_command("uptime")   # get info about working time and system load
    print(_stdout.read().decode())
    del client, _stdin, _stdout, _stderr                       # flash buffers


def changekey(host, key, localkey):
    host = host          #  Public IP Address
    username = "ubuntu"  # default user for ubuntu
    key = key + '.pem'   # ssh  private key
    pkey = paramiko.RSAKey.from_private_key_file(key) 
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(host, username=username, pkey=pkey)
    localkey = localkey   # public key for replacing
    with open(localkey, "r") as f:
        lkey = f.read()
    _stdin, _stdout, _stderr = \
        client.exec_command(f" echo '{lkey}'  > ~/.ssh/authorized_keys")  # replace key 
    print("public key replaced")


getmetrics(host, key)                                       # get info about system

changekey(host, key, localkey)                              # replace key 

terminateinstance(instance)                                # delete intance
