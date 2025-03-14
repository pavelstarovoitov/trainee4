"Задача №4 Nginx + Apache + PHP + SSL

Нужно реализовать обратный прокси на базе NGINX, который будет проксировать запросы: 
•что-то на локальную машину
•что-то на другой порт
•что-то на другой сервер.

1.Зарегистрируйся на сайте: https://www.dynu.com/
2.Разобраться в типах днс записей, и сделать днс запись типа А, для своего тестового сервера.
3.Затем используй 2 метода получения сертификатов для nginx.
4.Добавить редирект с 80 на 443 порт для всех подключений (cайт должен работать только по HTTPS).

В помощь:
Letsencrypt
webroot

Концепция такая:
Я стучусь на сервер (NGINX) по 80 порту и должен видеть описание, что-то типа:
•Если вы хотите попасть на страницу с контентом 1, то нажмите сюда (и мы попадаем на другую страничку, которую обрабатывает этот же NGINX просто по другому порту или днс имени).
•Если вы хотите скачать файл с музыкой нажмите сюда и по ссылке ты качаешь mp3. (IP/music)
•Если нужен сервер, работающий на Apache+PHP нажмите сюда и по ссылке отдаётся информация о PHP сервере (IP/info.php)
•Если вы хотите получить респонс с другого сервера жмите сюда и тут ты видишь уже сайт который отдается не проксёй, а другим сервером (IP/secondserver)
(4 дней)"

### Зарегистрируйся на сайте: https://www.dynu.com/

![image0001](image0001.png)

### Разобраться в типах днс записей, и сделать днс запись типа А, для своего тестового сервера.


![image0004](image0004.png)

![image0003](image0003.png)


### Затем используй 2 метода получения сертификатов для nginx

### Первый метод. Letsencrypt с использованием certbot
 
 sudo apt install certbot

 sudo apt install python3-certbot-nginx

 sudo certbot certonly --nginx -d trainee4.com
 
 sudo certbot certonly --nginx -d www.trainee4.com

![image0005](image0005.png)

### Второй метод. Сомоподписанный сертификат, использую openssl

sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt

![image0008](image0008.png)

![image0009](image0009.png)

![image0011](image0011.png)




### Добавить редирект с 80 на 443 порт для всех подключений (cайт должен работать только по HTTPS).

![image0014](image0014.png)
![image0013](image0013.png)



### Установка Apache и PHP

sudo apt install apache2


sudo apt install php libapache2-mod-php 

![image0015](image0015.png)

![image0016](image0016.png)

### Настройка location 

![image0017](image0017.png)

## [nginx.conf](nginx.conf)

![image0018](image0018.png)

![image0019](image0019.png)


## [index.html](index.html)

## [Cсылка на сайт](https://trainee4.com)














