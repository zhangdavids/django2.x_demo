


启动redis celery

    celery -A d_celery worker -l info



```

# 导入celery_app
from d_celery import celery_app

# 在异步执行的函数上加task装饰器
@celery_app.task
def your_function():
    pass

# 在视图函数中执行异步方法，
# 注意别忘了通过delay方法来实现异步调用
def index(request):
    your_function.delay()
    return HttpResponseRedirect('/')



```