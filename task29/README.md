Задача №29 Сделать http basic аутентификацию в nginx с хранением логина и пароля в ssm parameter store (1 день)

### Для создание логина и пароля устанaвливаю утилиту htpasswd

![image0001](image0001.png)

### Создаю логин и пароль в файле .htpasswd

![image0002](image0002.png)

### В nginx.conf указываю необходимость аутентификации

![image0003](image0003.png)

![image0004](image0004.png)

### Создаю секрет с логином и паролем  в ssm parameter store 

![image0005](image0005.png)

![image0006](image0006.png)

### Секрет можно получить с помощью aws cli 

![image0008](image0008.png)

### Удаляю файл .htpasswd где хранится логин и пароль и пересоздаю его из секрета ssm parameter store

![image0009](image0009.png)

