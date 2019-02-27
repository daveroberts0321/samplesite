from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {'insert_me' : "hello I am from views.py"}
    return render (request, 'sampleapp/index.html', context=my_dict)
def help(request):
    helpdict = {"insert_help": ' this is the help youre getting'}
    return render(request, 'sampleapp/help.html', context=helpdict)
