"Задача  №11 Задача на Application Load Balancer и домены

Практическая часть:
Нужно создать инстанс с nginx который работает на порту 80 или 443 отдает вашу кастомную вебстраничку.
Нужно создать инстанс с apache. который работает на порту 80 или 443 отдает вашу кастомную вебстраничку.
https://www.dynu.com/
https://www.noip.com/ нужно создать несколько записей у выбранного домена. Это будет иметь вид nginx.example.com и apache.example.com
*Под example.com понимается ваш купленный домен.

Нужно создать Application Load Balancer который разводит трафик в зависимости от того на какой хост приходит запрос. 
Если мы вводим в адресную строку браузера nginx.example.com то попадаем на наш инстанс с кастомной веб страничкой.
Если мы вводим в адресную строку браузера apache.example.com то попадаем на наш инстанс с кастомной веб страничкой.
Если мы вводим в адресную строку браузера google.example.com то попадаем на стартовую страницу поиска Гугл
Дедлайн 2 дня"

***
### Нужно создать инстанс с nginx который работает на порту 80 или 443 отдает вашу кастомную вебстраничку.

![image0001](image0001.png)

![image0002](image0002.png)

![image0003](image0003.png)

### Нужно создать инстанс с apache. который работает на порту 80 или 443 отдает вашу кастомную вебстраничку.

![image0005](image0005.png)
![image0006](image0006.png)
![image0007](image0007.png)

### https://www.dynu.com/ https://www.noip.com/ нужно создать несколько записей у выбранного домена. Это будет иметь вид nginx.example.com и apache.example.com *Под example.com понимается ваш купленный домен.

![image0008](image0008.png)
![image0009](image0009.png)
![image0010](image0010.png)
![image0011](image0011.png)

### Нужно создать Application Load Balancer который разводит трафик в зависимости от того на какой хост приходит запрос. 
Если мы вводим в адресную строку браузера nginx.example.com то попадаем на наш инстанс с кастомной веб страничкой.
Если мы вводим в адресную строку браузера apache.example.com то попадаем на наш инстанс с кастомной веб страничкой.
Если мы вводим в адресную строку браузера google.example.com то попадаем на стартовую страницу поиска Гугл

![image0012](image0012.png)

![image0013](image0013.png)

### Создаю CNAME records для Application Load Balancer
![image0019](image0019.png)

### Создаю target groups

![image0014](image0014.png)

![image0015](image0015.png)

### Создаю rules для Listener
![image0016](image0016.png)

### Routing выполняется по Host header
![image0017](image0017.png)

![image0018](image0018.png)

### Default rule

![image0020](image0020.png)


## [Default rule](http://myapploadbalancer-1118112336.us-east-1.elb.amazonaws.com/)

###  rule nginx.trainree4.com

![image0021](image0021.png)
## [rule if nginx.trainree4.com](http://nginx.trainee4.com/)


###  rule apache.trainree4.com
![image0022](image0022.png)

## [rule if apache.trainree4.com](http://apache.trainee4.com/)

###  rule google.trainree4.com
![image0023](image0023.png)

## [rule if google.trainree4.com](http://google.trainee4.com/)


