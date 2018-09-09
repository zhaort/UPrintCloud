from django.shortcuts import render

# Create your views here.


def index(requests):
    render(requests, 'FileRequest/index.html')
