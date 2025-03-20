"Задача №7  Создать 2 сервера, 1-ый паблик ( бастион хост) 2-ой сервер в приватке ( только приватный ИП, публичного нет) Скрипт , который при обращении на бастион
 Будет логиниться на приватный сервер и выполнять там команду апт гет апдейт ssh  . Также поставить варгард
 
уточнение по заданию:
у тебя на бастионе будет лежать скрипт, который я запущу по ссш, который выполнит команду ссш: подключись на приватный сервер и выполни ап апдейт (Дедлайн 3 дня)"
***
### Создаю VPC
![image0001](image0001.png)


![image0002](image0002.png)

### В новой VPC создаю две subnet. Public subnet для бастион хост, private subnet для  приватного хоста


![image0003](image0003.png)

![image0004](image0004.png)

### Создаю route tables для public и private subnet

![image0005](image0005.png)

![image0006](image0006.png)

![image0007](image0007.png)


![image0008](image0008.png)
### Создаю internet gateway для public subnet

![image0009](image0009.png)


![image0010](image0010.png)

![image0011](image0011.png)
![image0012](image0012.png)

### Создаю NAT getway для private subnet

![image0020](image0020.png)

![image0024](image0024.png)

### VPC имееет public и private subnet. 
### Трафик из/в public subnet роутится через route table и Internet gateway
### Трафик из/в private subnet роутится через route table и NAT gateway
### 

![image0023](image0023.png)
***
### Создаю бастион хост в public subnet

![image0013](image0013.png)

### Создаю приватный хост в private subnet

![image0014](image0014.png)

### Приватный хост не имеет public IP adress

![image0025](image0025.png)
***
### уточнение по заданию:
### у тебя на бастионе будет лежать скрипт, который я запущу по ссш, который выполнит команду ссш: подключись на приватный сервер и выполни ап апдейт 

### Подключаюсь к бастион хост по ssh 
![image0026](image0026.png)

### На бастион хост создаю скрипт который будет поключаться к приватному хосту и выполнять update

![image0027](image0027.png)

## [Файл Скрипта](update_script.sh)
### Команда ssh -i /home/ubuntu/.ssh/task7.pem ubuntu@10.0.1.250 выполняет подключение к приватному хосту
### 'sudo apt update -y && echo "Update was "$(date) >> script_run_log.log' выполняет обновление на приватном хосте и записывает дату и время выполнения в файл script_run_log.log

![image0028](image0028.png)

### Запускю скрипт на бастион хосте с локального компьютера

![image0029](image0029.png)

### Установка wireguard:

### На бастион хосте

![image0030](image0030.png)

![image0031](image0031.png)

### На приватном хосте

![image0032](image0032.png)










