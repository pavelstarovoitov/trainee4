"Задача  №17 по git (Д):
На основе преведущего задания настроить git hooks так что бы в случае коммита, будет отправленно письмо на электронную почту. *Чтобы принимать на gmail с github надо 2х факторная аутентификация
Дедлайн 1 день"

### Создаю ветку hooks в которой буду делать тестовые коммиты для отравки писем на почту

![image0001](image0001.png)

![image0002](image0002.png)

### В папке локального репозитория в .git/hooks создаю post-commit 
![image0016](image0016.png)


### В google.com получаю password для приложения

![image0006](image0006.png)

### Создаю скрипт на python для оправки сообщений 

![image0007](image0007.png)
## [sender.py](sender.py)
## [.env file](.env)


### Добавляю вызов python скрипта в .git/hooks/post-commit
![image0010](image0010.png)

![image0011](image0011.png)

## [post-commit](post-commit)

### Создаю GitHub Webhooks

![image0012](image0012.png)

### Создаю python flask скрипт на https://www.pythonanywhere.com/ чтобы получить url

![image0015](image0015.png)

## [pythonanywhere flask script](https://www.pythonanywhere.com/user/pavelstarovoitov91/shares/675e0480bce947ddb032b952be4aa5d1/)

![image0013](image0013.png)

![image0014](image0014.png)






