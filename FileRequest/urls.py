from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='fileRequestHome'),
    path('submit', views.submit, name='fileRequestSubmit'),
    path('download', views.download, name='fileRequestDownload'),
]
