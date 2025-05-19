Задача №25 Раскатить kubeadmin на сервере + запустить под nginx и достучаться до него (3 дня)


## На каждой из node:

### Отключаю swap 

![image0001](image0001.png)

### Включаю модули ядра
 
![image0002](image0002.png)

### Включаю ip forward 

![image0003](image0003.png)

### Применяю изменения
![image0004](image0004.png)

### Устанавливаю containerd 

![image0005](image0005.png)

![image0006](image0006.png)

![image0007](image0007.png)

![image0008](image0008.png)

![image0009](image0009.png)

![image0010](image0010.png)

### Устанавливаю  kubelet, kubeadm, kubectl

![image0011](image0011.png)

![image0012](image0012.png)

## На control panel node:

### Иницилизирую control panel кластера 

![image0013](image0013.png)

![image0014](image0014.png)

### Создаю конфиг файл кластера

![image0015](image0015.png)

![image0020](image0020.png)


### Устнавливаю CNI calico

![image0017](image0017.png)

![image0018](image0018.png)

## На worker node:

### Добавляю worker node к кластеру 

![image0016](image0016.png)

![image0019](image0019.png)


## На control panel node:

### Создаю namespace для приложений 

![image0021](image0021.png)

### Создаю deployment c nginx

![image0022](image0022.png)

![image0023](image0023.png)

![image0024](image0024.png)

![image0029](image0029.png)

![image0028](image0028.png)

# [deployment.yaml](deployment.yaml)

![image0030](image0030.png)

![image0031](image0031.png)

# [pod.yaml](pod.yaml)



### Создаю service типа NodePort для ngix-app deployment

![image0025](image0025.png)

![image0026](image0026.png)

![image0027](image0027.png)
![image0033](image0033.png)

![image0032](image0032.png)

# [service.yaml](service.yaml)



