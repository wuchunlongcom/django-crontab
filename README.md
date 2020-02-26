### django crontab定时执行任务             
### python3.7.5   django2.2.6  部署正常                      


### 主要步骤         
```
1、pip install django-crontab
requirements.txt 添加django-crontab

2、与view.py同级目录新建一个cron.py 
def test():
    print('hello world!')

3、settings.py中 
INSTALLED_APPS = [
     ...
    
    'django_crontab',
    'myAPI.apps.MyAPIConfig',   
    'account.apps.AccountConfig',
   
]
# 最后, 添加定时执行任务逻辑, 每分钟执行一次
CRONJOBS = [
    ('*/1 * * * *', 'account.cron.test', '>>/tmp/test.log')
]

4、start.sh
python3 "manage.py" "crontab" "add" # add
python3 "manage.py" "runserver" "8000"

5、创建文件/tmp/test.log

6、./start.sh -i

7、查看日记, 每分钟增加一个hello world!，证明程序运行正常！
vim /tmp/test.log

8、备注
停止运行工程，定时任务还在运行，若要停止定时任务，必须执行：删除所有定时任务命令 python mysite/manage.py crontab remove

```
### 显示当前的定时任务        
(env375) $ python mysite/manage.py crontab show
Currently active jobs in crontab:
b173a63adf4d670247b6b63dd93bc07b -> ('*/1 * * * *', 'account.cron.test', '>>/tmp/test.log')

### 删除所有定时任务  
(env375) $ python mysite/manage.py crontab remove
removing cronjob: (b173a63adf4d670247b6b63dd93bc07b) -> ('*/1 * * * *', 'account.cron.test', '>>/tmp/test.log')

### 重启django服务，执行 
crontab -e 
可以看到系统中创建了该定时任务。 