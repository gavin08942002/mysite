from django.http import HttpResponse
from django.shortcuts import render

def here(request):
    return HttpResponse('Mon I am here!')

def add(requst, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)
def math(request,a,b):
    a = float(a)
    b = float(b)
    s = a+b
    d = a-b
    p = a*b             
    q = a/b
    #html = '<html>sum = {s}<br>dif = {d}<br>pro = {p}<br> quoo = {q}</html>'.format(s=s,d=d,p=p,q=q)
    #return HttpResponse(html)
    return render(request,'math.html',locals())
def menu(request):
    food1={'name':'蕃茄炒蛋','price':'25','comment':'好吃','is _spicy':False}
    food2={'name':'蒜泥白肉','price':'100','comment':'人氣推薦','is _spicy':True}
    foods = [food1,food2]
#test
    return render(request,'menu.html',locals())
def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] !='':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        return render(request,'welcome.html',locals())

