module "vpc" {
  source = "./modules/vpc"
  
}


module "public_ec2" {
  source = "./modules/ec2"
  subnet_id = module.vpc.public_subnet_id
  security_groups_ids = [module.vpc.security_groups]
  

}

module "private_ec2" {
  source = "./modules/ec2"
  subnet_id = module.vpc.private_subnet_id
  security_groups_ids = [module.vpc.security_groups]
  
}

module "rds_postgres" {
  source = "./modules/rds"
}
