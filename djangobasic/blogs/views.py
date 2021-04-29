from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):

    return HttpResponse("<h1> HELLO WORLD </h1>")

def web(request):

    return render(request,'index.html',{'name':'บทความทำไงให้หล่อ',
    'author':'pinzaa'}) # web/index.html  in templates
