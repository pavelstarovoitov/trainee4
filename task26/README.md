Задача N26 Раскатить кластер куба через Kubespray, вывести информацию по доступным нодам, создать 3 namespace(test, dev, prod). Задеплоить микросервис(в вашем случае nginx) с помощью Kustomize для трех окружений( показать на главной старнице к какому окружению вы стучитесь) (5 дней)


# Создаю инстанс на котором будет работать ansible и уставливаю необходимые компоненты
![image0001](image0001.png)
![image0002](image0002.png)
![image0003](image0003.png)
![image0004](image0004.png)
![image0005](image0005.png)
![image0006](image0006.png)

# Копирую папку с темплайтами в папку mycluster
![image0007](image0007.png)

# В папке mycluster редоктирую файл inverntory.ini, добовляя в него ip адреса control plane и worker кластера. 
![image0008](image0008.png)
## [inventory.ini](inventory.ini)

# Запускаю playbook на создание кластера
![image0009](image0009.png)

![image0010](image0010.png)
![image0011](image0011.png)
# Информация по нодам 
![image0023](image0023.png)
![image0024](image0024.png)

# Создаю test, dev, prod namespaces
![image0013](image0013.png)

# Check kustomize
![image0012](image0012.png)

# Создаю дерево папок для kustomize

![image0014](image0014.png)
### [kustomize/base/deployment.yaml](kustomize/base/deployment.yaml)

### [kustomize/base/service.yaml](kustomize/base/service.yaml)

### [kustomize/base/kustomization.yaml](kustomize/base/kustomization.yaml)

### [kustomize/overlays/test/kustomization.yaml](kustomize/overlays/test/kustomization.yaml)

### [kustomize/overlays/dev/kustomization.yaml](kustomize/overlays/dev/kustomization.yaml)

### [kustomize/overlays/prod/kustomization.yaml](kustomize/overlays/prod/kustomization.yaml)


# Применяю изменения через kustomize

![image0015](image0015.png)
![image0016](image0016.png)
![image0017](image0017.png)

# Разворачиваю измененные .yaml файлы
![image0018](image0018.png)

![image0019](image0019.png)
![image0020](image0020.png)
![image0021](image0021.png)
![image0022](image0022.png)
