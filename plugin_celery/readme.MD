pro_cel
    ├── celery_task# celery相关文件夹
    │   ├── celery.py   # celery连接和配置相关文件,必须叫这个名字
    │   └── tasks1.py    #  所有任务函数
    │	└── tasks2.py    #  所有任务函数
    ├── check_result.py # 检查结果
    └── send_task.py    # 触发任务,如django调用 (快递的投递)

​	└── worker.py    # 开启run_worker,异步执行(快递的运输)