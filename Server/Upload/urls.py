from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='uploadHome'),  # 上传文件的页面
    path('submit', views.submit, name='uploadSubmit')  # 接受上传文件的请求
]
