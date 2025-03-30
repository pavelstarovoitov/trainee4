terraform {
  required_version = ">= 1.10"
}


resource "aws_vpc" "main" {
  cidr_block = "10.5.0.0/16"
  instance_tenancy = "default"
  enable_dns_support = "true"
  enable_dns_hostnames = "true"
  tags = {
    Name = "my terraform vpc"
  
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id = aws_vpc.main.id
  cidr_block = "10.5.1.0/24"
  map_public_ip_on_launch = "true"
  availability_zone = var.ZONE1
  tags = {
    Name = "public_subnet"
  }
}

resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.main.id
  cidr_block = "10.5.2.0/24"
  map_public_ip_on_launch = "true"
  availability_zone = var.ZONE1
  tags = {
    Name = "private_subnet"
  }
}


resource "aws_internet_gateway" "IGW" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "my IGW"
  }
  
}

resource "aws_nat_gateway" "NatGW" {
  subnet_id = aws_subnet.public_subnet.id
  allocation_id = aws_eip.forNatGW.id
  tags = {
    Name = "my NatGW"
  }

}

resource "aws_eip" "forNatGW" {
  #vpc = true
  domain = "vpc"
}

resource "aws_route_table" "public_RT" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.IGW.id
  }
  
  tags = {
    Name = "Public_RT"
  }
}

resource "aws_route_table" "private_RT" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.NatGW.id
  }

  tags = {
    Name = "Private_RT"
  }

}

resource "aws_route_table_association" "public_subnet" {
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_RT.id
  
}

resource "aws_route_table_association" "private_subnet_association" {
  subnet_id = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private_RT.id
}

resource "aws_security_group" "terraform_sg" {
    name = "allow_ssh"
    description = "sg for allowing ssh"
    vpc_id = aws_vpc.main.id

    tags = {
      Name = "terraform security group"
    }
  
}

#####################################33
## security group rule###
resource "aws_security_group_rule" "for_ssh_terraform_ing" {
  type  = "ingress"
  from_port = 22
  to_port = 22
  protocol = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.terraform_sg.id
}

resource "aws_security_group_rule" "for_ssh_terraform_egr" {
  type  = "egress"
  from_port = 22
  to_port = 22
  protocol = "-1"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.terraform_sg.id
}
