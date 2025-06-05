Задача №27 Перенести всю структуру с докера на куб,а конфиг через конфиг мап. + добавить liness,readness, startup probe(Дедлайн 4 дня). 


### Разворачиваю кластер с помощью kubespray. В addons.yml выбираю metallb и ingress для установки

![image0001](image0001.png)

![image0002](image0002.png)

### В k8s-cluster.yml указываю kube_proxy_strict_arp: true для metallb

![image0003](image0003.png)

### В  addons.yml указываю local_volume_provisioner_enabled: true для монтирования configmap

![image0004](image0004.png)

### В inventory.ini указываю ip адреса нодов

![image0005](image0005.png)

#### Запускаю ansible-playbook и разворачию кластер

![image0006](image0006.png)

#### Добавляю IPAddressPool для metallb

![image0007](image0007.png)

## [addresspool.yaml](addresspool.yaml)

![image0008](image0008.png)

### Создаю секрет для докер registry 

![image0009](image0009.png)



### Создаю секрет для ingress использую ssl сертификат и ключ
![image0010](image0010.png)

![image0011](image0011.png)


### Создаю configmap для nginx.conf и index.html файлов

![image0012](image0012.png)

## [configmap2.yml](configmap2.yaml)

![image0013](image0013.png)

## [configmap.yml](configmap.yml)


### Создаю deployment nginx

![image0014](image0014.png)

## [deployment.yaml](deployment.yaml)

### В deployment указываю volumeMounts для configmap и readiness, liveness, starup Probes
![image0015](image0015.png)

### Для probes создаю location в nginx.conf

![image0028](image0028.png)

### Создаю ingress для https трафика

![image0016](image0016.png)

## [ingress.yaml](ingress.yaml)


### Создаю nginx-service типа LoadBalancer

![image0017](image0017.png)

## [service.yaml](service.yaml)


### Создаю ingress для http трафика

![image0018](image0018.png)

## [ingress2.yaml](ingress2.yaml)

###  Создаю deployment для  apache

![image0019](image0019.png)

## [deploymentapache.yaml](deploymentapache.yaml)

###  Создаю service для  apache

![image0030](image0030.png)

## [serviceapache.yaml](serviceapache.yaml)

### Проверяю запущенные ресурсы

![image0020](image0020.png)

### Обновляю DNS записи 

![image0021](image0021.png)

### Проверяю работу

![image0022](image0022.png)

![image0023](image0023.png)

![image0024](image0024.png)

![image0025](image0025.png)

![image0026](image0026.png)

![image0027](image0027.png)


### Прверяю ответ /healthz  для probes

![image0029](image0029.png)















