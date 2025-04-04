Задача  №15 ECS:  перенести структуру докера в ecs. в ec2 и в fargate. Тип не таск, а сервис. + Подвязать application load balancer Дедлайн 2 дня

### Создаю fargete cluster

![image0002](image0002.png)

### Создаю task definition для fargete cluster
![image0003](image0003.png)

![image0004](image0004.png)


![image0005](image0005.png)
### Создаю Serivce использую созданную task 
![image0006](image0006.png)

![image0007](image0007.png)
### Проверяю запущенну taks
![image0008](image0008.png)
![image0009](image0009.png)
![image0010](image0010.png)
### Создаю EC2 cluster
![image0011](image0011.png)

### Создаю task definition для EC2 cluster

![image0012](image0012.png)

![image0013](image0013.png)

![image0014](image0014.png)
### Создаю Service для EC2 cluster
![image0015](image0015.png)
### Проверяю запущенну taks для EC2 cluster
![image0016](image0016.png)
![image0018](image0018.png)

## + Подвязать application load balancer

### Создаю Service для EC Cluster c load balancer
![image0019](image0019.png)

![image0020](image0020.png)


### Создаю Service для fargete c load balancer
![image0022](image0022.png)
![image0021](image0021.png)
