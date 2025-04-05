"Задача  №16 по git (Д):
""пункт 1""
Надо взять уже имеющейся проект, залить его в гитхаб. Залить в ветку master(main), создать ветку develop, внести изменение в файлы в develop и сделать pull request(merge request) в master(main). 
Подключение к гиту должно быть с помощью ssh-key. Все изменения производить в консоле. На чеке от ментора показать откат коммита в дев ветке и так же сделать pull request(merge request).
""пункт 2"":
Подолжая работу с проектом создать 5 коммитов в develop ветке, и в ветку prod записать только 1-й,3-й,5-й коммиты, которые были сделаны в develop
Дедлайн 1 день""

##""пункт 1""
### Иницилизирую локальный  git репозиторий с веткой main. 
![image0001](image0001.png)

### Делаю init commit  
![image0002](image0002.png)

### Добавлюя ssh ключ на github аккаунт

![image0003](image0003.png)

![image0004](image0004.png)

### Устанавливаю gh 
![image0005](image0005.png)

![image0006](image0006.png)

### Создаю репозиторий на github

![image0007](image0007.png)

![image0008](image0008.png)

![image0009](image0009.png)

### Копирую файлы из локального репозитория на github в ветку main

![image0011](image0011.png)

![image0010](image0010.png)

### Создаю ветку develop 

![image0012](image0012.png)

### Вношу изменения в файл README.md

![image0013](image0013.png)

![image0014](image0014.png)
### Добавляю ветку develop на github

![image0015](image0015.png)

### Создаю merge requst

![image0016](image0016.png)

![image0017](image0017.png)

![image0018](image0018.png)

***
## ""пункт 2""
### Cоздаю 5 коммитов в develop ветке

![image0019](image0019.png)


### Cоздаю ветку prod

![image0020](image0020.png)

### C помощью команды git rebase -i оставляю только 1-й, 3-й и 5-й коммиты

![image0023](image0023.png)
![image0021](image0021.png)

![image0022](image0022.png)

### Копирую ветку prod на github

![image0025](image0025.png)

![image0024](image0024.png)

## [Cсылка на репозиторий в github](https://github.com/pavelstarovoitov/project/tree/develop)


