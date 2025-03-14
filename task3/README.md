### Задача №3 

 1. В EC2 установить free-tire ubuntu и накатить на неё NGINX
 2. Создать репозиторий на GitHub для дальнейшей работы(сохранение всех конфигов nginx, docker и тд...) (Дедлайн 1 день) 

### Создание free-tire ubuntu
![image0003](image0003.png)

![image0004](image0004.png)


### Конфигурация Inbound Outbound правил в Security Groups


![image0005](image0005.png)
![image0006](image0006.png)


### Установка Nginx

sudo apt get update 

sudo apt install nginx

![image0001](image0007.png)


### Настройка фаервола ufw

sudo ufw app list

sudo ufw allow 'Nginx Full'

sudo ufw enable

sudo ufw status

![image0010](image0010.png)

### Проверка nginx

sudo systemctl status nginx

curl 54.221.128.94

![image0003](image0009.png)






