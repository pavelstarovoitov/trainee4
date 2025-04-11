Задача №21 Третий таск. Поднять в композде локи/промтейл Настроить вывод логов с nginx. Прочитать логи (можно через графану например). Делать отдельнно от преведущих задач - 1день

### Создаю docker-compose.yml для сервисов loki и promtail

![image0001](image0001.png)

## [docker-compose.yml](docker-compose.yml)

### В volumes:loki  сервис loki хранит свои рабочие файлы

![image0011](image0011.png)

###  Cервис promtail получает доступ к логам nginx через  монтирование - /var/log/nginx:/logs

![image0012](image0012.png)

### В папках loki_conf promtail_conf храняться файлы конфигурации для сервисов.

![image0002](image0002.png)

## [./loki_conf/local-config.yaml](./loki_conf/local-config.yaml)

![image0009](image0009.png)

## [./promtail_conf/config.yaml](./promtail_conf/config.yml)

![image0010](image0010.png)



### Запускаю docker-compose.yml и проверяю сервисы

![image0003](image0003.png)

![image0004](image0004.png)

### Подключаю источник данных loki в Grafana

![image0005](image0005.png)

### Создаю дашборд и читаю данные от loki

![image0007](image0007.png)

### Данные можно выбирать как по job так и по имени файла или имени сервиса

![image0008](image0008.png)