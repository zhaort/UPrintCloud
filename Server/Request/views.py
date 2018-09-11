from django.shortcuts import render, HttpResponse
from django.http import FileResponse
import os
from . import lib
# Create your views here.


def index(requests):
    if requests.method == 'GET':
        data = {
            'url': 'http://127.0.0.1:8000/print/',
        }
        return render(requests, 'Request/index.html', data)
    return HttpResponse('Hello World!')


def submit(requests):
    if requests.method == 'POST':
        key = requests.POST.get('key', -1)
        url = requests.POST.get('url', -1)
        if key != -1 and url != -1:
            file = lib.getFile(key)
            if file != -1:
                lib.sendRequest(url, file)
                return HttpResponse('Success')
    return HttpResponse(404)


def download(requests, filename):
    sep = os.path.sep
    path = 'usr%sdownloads%s%s' % (sep, sep, filename)
    file = open(path, 'rb')
    response = FileResponse(file)
    # os.remove(path)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="file.pdf"'
    return response
