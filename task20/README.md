Задача №20 Второй таск. Поднять ещё один инстанс. Туда подключить экспортер с помощью docker или docker-compose. В прометеусе сделать задачи по лейблам алерта. СPU с одного инстанса, оперативка чекается с другого инстанса. Алерты в слак. (1 день)

### Создаю инстанс в EC2 
![image0003](image0003.png)
### На инстансе создают docker-compose.yml и запускаю в нем node_exporter
![image0001](image0001.png)
![image0004](image0004.png)
### В файле конфигурации prometheus.yml добавлюя новый job 
![image0005](image0005.png)
## [prometheus.yml ](./prometheus_volume/prometheus.yml )
### В файле конфигурации rules.yml добавлюя новый alert HighMemoryUsage

![image0006](image0006.png)

## [rules.yml ](./prometheus_volume/rules.yml )

### Правило HighMemoryUsage проверяет память на job='node2', тоеть только на новом инстансе

### В файле конфигурации alertmanager.yml  настраиваю оповещения в slack 

![image0007](image0007.png)
![image0002](image0002.png)

## [alertmanager.yml ](./alertmanager_volume/alertmanager.yml )

### Интерфейс prometeus где можно отладить условия на алерты
![image0008](image0008.png)