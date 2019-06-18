from celery import Celery

cel = Celery('celery_demo', broker='redis://127.0.0.1:6379/1', backend='redis://127.0.0.1:6379/2',
            include=['celery_task.task_send_email','celery_task.task_send_code_phone'])

#时区
cel.conf.timezone = 'Asia/Shanghai'

#不使用UTC
cel.conf.enable_utc = False

#配置定时任务,也可以是调用执行函数时
