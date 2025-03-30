variable "instance_name" {
    description = "EC2 instance name"
    type = string
    default = "MY_terrafrom_instance"
  
}

variable "ami" {
    description = "ami"
    type = string 
    default = "ami-084568db4383264d4"
  
}

variable "instance_type" {
    description = "instance_type"
    type = string 
    default = "t2.micro"
  
}

variable "key_name" {
    description = "key_name"
    type = string 
    default = "task2"
  
}

variable "subnet_id" {
    description = "subnet_id"
    type = string 
  
}

variable "security_groups_ids" {
    description = "security_group"
    type = list(string)
    
  
}


