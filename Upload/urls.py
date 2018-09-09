from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='uploadHome'),
    path('submit.do', views.submit, name='uploadSubmit')
]
