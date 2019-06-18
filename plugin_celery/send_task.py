from celery_task.task_send_email import send_email

# 立即告知celery去执行delay()方法test_celery任务，并传入一个参数,意不执行apply_async
result = send_email.apply_async(['1132424753@qq.com'])
print(result.id) #可用于django调用
