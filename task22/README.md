"Задача №22 Четвёртый таск. Поднять графану /Прометеус / нод-экспортер / локи/промтейл Законектить Прометеус и локи в графану . Настроить дашборты по cpu и оперативы.
 Настроить дашборт по логам nginx и апатч. Настроить нотификацию в слак через графану. Делать через docker-compose. 2 дня"


### Создаю docker-compose.yml для сервисов

![image0001](image0001.png)

![image0003](image0003.png)

![image0004](image0004.png)

![image0005](image0005.png)

![image0006](image0006.png)

![image0007](image0007.png)


## [docker-compose.yml](./docker-compose.yml)

### Создаю дополнительную виртуальную машину для на которой будет мониториться оперативная память и запускаю на ней node_exporter

![image0002](image0002.png)


### Так как оповещение о алертах будет выполнятся через grafana убираю из конфигурации prometheus.yml  указание на alertmanager и меняю ip адрес для node2  

![image0008](image0008.png)

## [./prometheus_volume/prometeus.yml](./prometheus_volume/prometheus.yml)

### В файл конфурации config.yml для сервиса promtail добавляю job apache2_log для чтения логов apache2

![image0009](image0009.png)

## [./promtail_conf/config.yml](./promtail_conf/config.yml)

### В grafana добавляю data source для loki и prometheus

![image0015](image0015.png)

![image0016](image0016.png)


### Настраиваю contact point для slack
![image0010](image0010.png)

### Cоздаю алерты для CPU и Memory
![image0013](image0013.png)

![image0014](image0014.png)

![image0011](image0011.png)

![image0012](image0012.png)

### Создаю дашборды для мониторинга CPU, Memory, логов nginx и apache2

![image0017](image0017.png)

![image0019](image0019.png)


![image0018](image0018.png)

![image0020](image0020.png)





