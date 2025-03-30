terraform {
  required_version = ">= 1.10"
}


resource "aws_db_instance" "posgress" {
    count = 1
    identifier =  "mypostgres-${count.index}"
    allocated_storage = 20
    instance_class = "db.t3.micro"
    engine_version = "17.2"
    engine = "postgres"
    #username = var.username
    #password = var.password
    username = "postgres"
    password = "qw005870"
    multi_az = true
    skip_final_snapshot = true
    publicly_accessible = true
    #db_subnet_group_name = aws_db_subnet_group.db_subnet_for_postgres.id
  
}
/*
resource "aws_db_subnet_group" "db_subnet_for_postgres" {
  name = "db subnet for posgres"
  description = "private subnet for posgres"
  subnet_ids = [aws_subnet.private_subnet.id]
}
*/
