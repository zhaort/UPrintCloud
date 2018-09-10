from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='requestHome'),
    path('submit', views.submit, name='requestSubmit'),
    path('download/<str:filename>', views.download, name='requestDownload'),
]
