from celery_task.celery import cel
if __name__ == '__main__':
    cel.worker_main(argv=['--loglevel=info','--pool=eventlet'])