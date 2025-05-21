Задача N25* Раскатить кластер куба через k3s.Прочитать документацию k3s и знать разницу Deckhouse (3 дня)

### Уставливаю k3s на master node.

![image0001](image0001.png)

### Получаю node token 

![image0002](image0002.png)

### Зная ip адрес macter node и node token, добавляю к кластеру worker node

![image0003](image0003.png)

![image0004](image0004.png)

### Создаю сервис типа NodePort и Deployment для nginx

![image0005](image0005.png)

## [nginx.yaml](nginx.yaml)

![image0006](image0006.png)

![image0007](image0007.png)

![image0008](image0008.png)








