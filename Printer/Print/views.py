from django.shortcuts import render, HttpResponse
from requests import get
import os

# Create your views here.


def index(requests):
    if requests.method == 'GET':
        filename = requests.GET.get('file', -1)
        if filename != -1:
            url = 'http://127.0.0.1:8001/request/download/%s' % filename
            req = get(url)
            with open('usr%sbuf.pdf' % (os.path.sep), 'wb') as file:
                file.write(req.content)
    return HttpResponse(404)
