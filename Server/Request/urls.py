from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='uploadHome'),
    path('submit', views.submit, name='uploadSubmit')
]
