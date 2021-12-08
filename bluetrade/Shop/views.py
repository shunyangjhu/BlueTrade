from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .models import *
import datetime
import json


# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)


def AllCommodity(request):
    commodities = Commodity.objects.all()
    print(commodities)
    return HttpResponse(commodities)


def AllUser(request):
    users = User.objects.all()
    print(users)
    return HttpResponse(users)

def user_login(request):
    if request.method == "POST":
        body = json.loads(request.body)
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        email = body['email']
        password = body['password']
        user = User.objects.get(email=email)
        if password == user.password:
            message = 'login success!'
            code = 200
        else:
            message = 'login failed'
            code = 404
    else:
        message = "POST method is required but not used."
        code = 404

    response = {"data": message, "code": code}
    return HttpResponse(json.dumps(response), content_type='application/json')



def user_register(request):
    if request.method == "POST":
        body = json.loads(request.body)
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        name = body['name']
        email = body['email']
        password = body['password']
        user = User()
        user.name = name
        user.email = email
        user.password = password
        user.save()
    return render(request, 'user/register.html')
