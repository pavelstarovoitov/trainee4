"Задача №28  Поднять графану /Прометеус / нод-экспортер / локи/промтейл в кубе Понднятие мониторинга будет происходить через Helm 
Законектить Прометеус и локи в графану . Настроить дашборты по cpu и оперативы. Настроить дашборт по логам nginx и апатч. Настроить нотификацию 
в слак через графану. + настроить PVC (4 дня)
Возможно получение проблемы дефолтного чарта проблема версий связки grafana + loki, графана зафиксирована а локи последней ревизии не совпадают( фикс либо апгрейд, либо даунгрейд версии)" 

## Так как поднятие мониторинга будет происходить через Helm, то в  файле addons.yml кубспрэя выбираю helm для установки 

![image0011](image0011.png)

## С помощью кубспрэя  создаю кластер

![image0016](image0016.png)

![image0018](image0018.png)

## Добавляю репозитории для графана/локи и прометеус/графана

![image0020](image0020.png)

## Создаю namespace для мониторинга

![image0017](image0017.png)

## Для локи создаю PV and PVC

# [loki-pv.yml](loki-pv.yml)

# [storage-loki-0.yml](storage-loki-0.yml)

![image0027](image0027.png)

## Устанавливаю локи

![image0021](image0021.png)

### файл с параметрами установки локи

# [loki-values.yml](loki-values.yml)

### Локальная папка на worker node где локи создал свои файлы

![image0026](image0026.png)


## Устанавливаю promtail 

![image0023](image0023.png)


## Устанавливаю графана, прометеус, нод-эскпортер 

![image0022](image0022.png)

![image0024](image0024.png)

![image0025](image0025.png)

## Для графана, прометеус, нод-эскпортер  создаю PV and PVC

# [prom-pv.yml](prom-pv.yml)

# [prom-pvc.yml](prom-pvc.yml)

# [kube-stack-values.yml](kube-stack-values.yml)

![image0033](image0033.png)

![image0032](image0032.png)

![image0031](image0031.png)

![image0030](image0030.png)

![image0029](image0029.png)



## Законектить Прометеус и локи в графану 

![image0012](image0012.png)

![image0013](image0013.png)

![image0014](image0014.png)

![image0015](image0015.png)

## Настроить дашборт по логам nginx и апатч.

![image0001](image0001.png)

![image0002](image0002.png)

## Настроить дашборты по cpu и оперативы.

![image0003](image0003.png)

![image0004](image0004.png)

## Настроить нотификацию в слак через графану

![image0007](image0007.png)

![image0006](image0006.png)

![image0005](image0005.png)

![image0008](image0008.png)

![image0009](image0009.png)

![image0010](image0010.png)