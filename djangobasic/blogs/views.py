from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''
def hello(request):

    return HttpResponse("<h1> HELLO WORLD </h1>")
'''
def hello(request):
    tags = ['หล่อ','รวย','เท่']
    age = 36
    txt = "My name is John, and I am {}"
    text1 = txt.format(age)
    rateing = 4
    
    return render(request,'index.html',
    {
        'name':'บทความทำไงให้หล่อ',
        'author':'pinzaa',
        'tags':tags,
        'text':text1,
        'rateing':rateing
    }) # web/index.html  in templates

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request, 'form.html')

def addBlog(request):
    name = request.POST['name']
    description = request.POST['description']
    return render(request, 'result.html',
    {
        'name':name,
        'description':description
    
    })
