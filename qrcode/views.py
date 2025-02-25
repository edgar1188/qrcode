from django.shortcuts import render
from django.http import HttpResponse
import pyqrcode
from io import BytesIO

# Create your views here.


def index(request):
    return render(request,'qrcode/index.html')

def qrcode(request,ssid,password):
    qr = pyqrcode.create(f'WIFI:S:{ssid};T:WPA;P:{password};;')
    buffer = BytesIO()
    qr.png(buffer,scale=15)
    return  HttpResponse(buffer.getvalue(),content_type='image/png')