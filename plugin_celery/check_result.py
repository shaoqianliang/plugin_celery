from celery_task.celery import cel
from celery.result import AsyncResult
async = AsyncResult(id='addc82c3-900f-400b-ba44-3c5590694776',app=cel) #根据id获取结果
if async.successful():
    result = async.get()
elif async.failed():
    print('执行失败')
elif async.status == 'PENDING':
    print('任务等待中被执行')
elif async.status == 'RETRY':
    print('任务异常后正在重试')
elif async.status == 'STARTED':
    print('任务已经开始被执行')