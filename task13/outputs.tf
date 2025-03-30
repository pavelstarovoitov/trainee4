
output "private_instance_id" {
  description = "ID of the EC2 instance"
  value = module.private_ec2.instance_id
}
output "public_instance_id" {
  description = "ID of the EC2 instance"
  value = module.public_ec2.instance_id
}


output "private_private_ip" {
  description = "ID of the EC2 instance"
  value = module.private_ec2.instance_public_ip
}


output "public_public_ip" {
    description = "Public IP address of the EC2 instance"
    value = module.public_ec2.instance_public_ip
  
}

