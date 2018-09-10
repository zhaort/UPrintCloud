from django.shortcuts import render, HttpResponse
from . import lib

# Create your views here.


def index(requests):
    return render(requests, 'FileRequest/index.html')


def submit(requests):
    ret = -1
    if requests.method == 'GET':
        ret = lib.getFile(requests.GET.get('key', -1))
    return HttpResponse(ret)


def download(requests):
    pass
