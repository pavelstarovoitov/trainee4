"Задача  №9 для IAM (И)

Часть 1
Создать EC2 инстанс и s3 bucket c именем mybucket. Сделать так чтоб доступ был к ведру mybucket был через IAM роль.
Когда вводим aws s3 ls мы должны увидеть список ведер
*Не пользуемся AWS configure и не делаем export переменных для кредов аккаунта AWS 

Часть 2
Создать в IAM пользователя Petr и предоставить емуConsole access. Cоздать группу just_users. Добавить пользователя в группу just_users. Дать 
права группе на только на полный доступ к EC2. Попробовать из этого пользователя Petr создать новый инстанс в любом регионе и создать vpc в любом 
регионе. Рассказать о результах

*Часть 1 и Часть 2 не связаны друг с другом
Дедлайн 3 дня"

### Часть 1

### Создаю Policy
![image0001](image0001.png)

![image0002](image0002.png)

![image0003](image0003.png)

## [Policy for S3 bucket](s3_policy.json)

### Создаю Role для EC2

![image0004](image0004.png)

![image0005](image0005.png)

### Создаю инстансе EC2 с ролью для просмотра S3 bucket

![image0006](image0006.png)

### Создаю S3 bucket

![image0007](image0007.png)

![image0008](image0008.png)

### Когда вводим aws s3 ls мы должны увидеть список ведер

![image0009](image0009.png)

***

### Часть 2

### Создать в IAM пользователя Petr и предоставить емуConsole access.

![image0010](image0010.png)

![image0011](image0011.png)

![image0012](image0012.png)

![image0013](image0013.png)

![image0014](image0014.png)

## [AmazonEC2FullAccess.json](AmazonEC2FullAccess.json)

![image0015](image0015.png)

![image0016](image0016.png)

### Попробовать из этого пользователя Petr создать новый инстанс в любом регионе и создать vpc в любом регионе. Рассказать о результах

![image0017](image0017.png)

![image0018](image0018.png)

### Пользователь Petr имеет возможность создовать инстансы EC2 и VPC, так как правило AmazonEC2FullAccess включает не только доступ к EC2, но и к другим сервисам 

![image0019](image0019.png)














