"Задача №8 про AWS RDS

Создать инстанс для базы данных типа postgres с именем cluster_jun. Подключится к ней через pgAdmin установленный на ПК и через командную строке терминала линукс через терминальный клиент psql. Cоздать в кластере баз данных postgres базу данных jun_db. Создать в ней таблицу под названием credit_cards_numbers. 

Руками сделать snapshot. Удалить базу данных. Восстановить её из snapshots. Проверить наличие созданной таблицы через pgAdmin и терминальный клиент psql.

Настроить её бэкапы через AWS Backup по расписанию раз в час например. Когда сделан автоматический backup удалить текущий кластер баз данных jun_db и восстановить его из бэкапа. Проверить наличие созданной таблицы credit_cards_numbers через pgAdmin и терминальный клиент psql. Дедлайн 2 дня"
NEW

***
### Создаю инстанс базы данных postgresql

![image0002](image0002.png)

![image0003](image0003.png)

#### Создаю Inbound rule для postrgesql порт 5432

![image0004](image0004.png)

### Устанавливаю psql на локальной машине и подключаюсть к postgres инстансу в AWS

![image0005](image0005.png)
![image0006](image0006.png)

### Устанавливаю pgAdmin4 на локальной машине и подключаюсть к postgres инстансу в AWS
![image0007](image0007.png)

### Cоздать в кластере баз данных postgres базу данных jun_db. Создать в ней таблицу под названием credit_cards_numbers. 

![image0008](image0008.png)

![image0009](image0009.png)

![image0010](image0010.png)

![image0011](image0011.png)

### Руками сделать snapshot. Удалить базу данных. Восстановить её из snapshots. Проверить наличие созданной таблицы через pgAdmin и терминальный клиент psql.

![image0012](image0012.png)

![image0013](image0013.png)

![image0016](image0016.png)

![image0017](image0017.png)

![image0018](image0018.png)

![image0019](image0019.png)

![image0020](image0020.png)

### Настроить её бэкапы через AWS Backup по расписанию раз в час например. Когда сделан автоматический backup удалить текущий кластер баз данных jun_db и восстановить его из бэкапа. Проверить наличие созданной таблицы credit_cards_numbers через pgAdmin и терминальный клиент psql.

![image0014](image0014.png)

![image0015](image0015.png)

![image0022](image0022.png)

![image0023](image0023.png)

![image0024](image0024.png)
![image0028](image0028.png)

![image0025](image0025.png)

![image0026](image0026.png)

![image0027](image0027.png)


