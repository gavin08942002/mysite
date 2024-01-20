from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from requests import Request
import requests
from restaurants.models import Restaurant,Food

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
    if 'id' in request.GET and request.GET['id'] !='':
        restaurant = Restaurant.objects.get(id = request.GET['id'])
        return render(request,"menu.html",locals())
    else:        
        return HttpResponseRedirect("/restaurants_list")


def meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k,v))
        return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))


def menu1(request):
    food1={'name':'蕃茄炒蛋','price':'25','comment':'好吃','is _spicy':False}
    food2={'name':'蒜泥白肉','price':'100','comment':'人氣推薦','is _spicy':True}
    foods = [food1,food2]

    return render(request,'menu.html',locals())


def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request,'restaurants_list.html',locals())