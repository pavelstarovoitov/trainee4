"Задача N26* Добавить к предыдущей задаче установку metrics-server + развернуть в кластере Kubernetes Dashboard. Обратить внимание на версию Kubernetes и его поддерживаемую версию со стороны Kubernetes Dashboard. Посмотреть, что он из себя представляет. 
Установить себе на локальную машину Kubernetes Lens IDE, подключить свой кластер Kubernetes, и также посмотреть, что из себя представляет приложение
. (2 дня)"

### В файле /home/ubuntu/kubespray/inventory/mycluster/group_vars/k8s_cluster/addons.yml делаю доступными для установки dashboard и mertrics_server. Меняю порт с 10250 на 4443, так как 10250 испозльуется kubelet

![image0001](image0001.png)

## [addons.yml](addons.yml)

![image0015](image0015.png)


### Редактирую Service дашборда с ClusterIP на NodePort

![image0011](image0011.png)

#### Создаю ServiceAccount для просмотра дашборда

![image0012](image0012.png)

## [kubernetes-dashboard-admin-user.yml](kubernetes-dashboard-admin-user.yml)


#### Создаю token

![image0013](image0013.png)

![image0014](image0014.png)

### Обратить внимание на версию Kubernetes и его поддерживаемую версию со стороны Kubernetes Dashboard. 

![image0002](image0002.png)


### Версия кластера 1.32.5 

![image0003](image0003.png)
![image0004](image0004.png)

### Версия dashboard 2.7.0

![image0005](image0005.png)


### Посмотреть, что он из себя представляет. 

### Действия доспутные пользoвателю определяются исходя из RBAC  пользователя. В общем случае доступен следующий функционал:
### Dashboard позволяет просматривать сущность кластер, позволяет изменять просматриваеный namespace

![image0006](image0006.png)

### Позволяет подключатся к поду черес команду exec

![image0007](image0007.png)

### Позволяет просматривать логи пода

![image0008](image0008.png)

### Позволяет редактировать  сущности кластера

![image0009](image0009.png)

### Установить себе на локальную машину Kubernetes Lens IDE, подключить свой кластер Kubernetes, и также посмотреть, что из себя представляет приложение

![image0016](image0016.png)

### Копирую конфиг файл кластера с control-plane ноды на локальную машину

![image0023](image0023.png)


### Добавляю файл конфигурации кластера в Lens

![image0017](image0017.png)


### Указываю публичный ip адрес control-plane ноды в конфиг файле кластера

![image0018](image0018.png)

### Делаю Port Forwarding на контрол ноде

![image0019](image0019.png)

### Lens отображает сущности кластера 
![image0020](image0020.png)

### В Lens можно просматривать иcпользавание ресурсов кластером, редактировать сущности кластера, просматривать логи, подключаться к подам. 

![image0021](image0021.png)

![image0022](image0022.png)










