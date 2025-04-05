"Задача  №17 по git (Д):
На основе преведущего задания настроить git hooks так что бы в случае коммита, будет отправленно письмо на электронную почту. *Чтобы принимать на gmail с github надо 2х факторная аутентификация
Дедлайн 1 день"

### Создаю ветку hooks в которой буду делать тестовые коммиты для отравки писем на почту

![image0001](image0001.png)

![image0002](image0002.png)

### Папке локального репозитория в .git/hooks переименоваю commit-msg.sample в commit-msg
![image0003](image0003.png)

### Редоктирую commit-msg скрипт

![image0004](image0004.png)

### Теперь при выполнении git commit появляется измененное сообщение

![image0005](image0005.png)

### В google.com получаю password для приложения

![image0006](image0006.png)

### Создаю скрипт на python для оправки сообщений 

![image0007](image0007.png)
## [sender.py](sender.py)
## [.env file](.env)


### Добавляю вызов python скрипта в .git/hooks/commit-msg
![image0010](image0010.png)

![image0011](image0011.png)

## [commit-msg](commit-msg)





