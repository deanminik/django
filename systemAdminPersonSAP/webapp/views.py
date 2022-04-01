from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcomefunction(request):
    return HttpResponse('Hello world from django')

def saybye(request):
    return HttpResponse('Saying bye from django')
