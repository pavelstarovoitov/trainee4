output "vpc_id" {
    description = "out vpc_id"
    value = aws_vpc.main.id
  
}

output "public_subnet_id" {
  description = "subnet_id"
  value = aws_subnet.public_subnet.id
}

output "private_subnet_id" {
  description = "subnet_id"
  value = aws_subnet.private_subnet.id
}

output "security_groups" {
    description = "security_groups"
    value = aws_security_group.terraform_sg.id
  
}