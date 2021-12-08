from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

import json
from collections import defaultdict


from .models import *


def getInfo(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body["email"]
        # print(email)
        user = User.objects.filter(email=email).get()
        avatarurl = None
        if user.avatarurl != "":
            avatarurl = user.avatarurl

        temp = {"name": user.name, "email": user.email,
                "password": str(user.password), "phone": str(user.phone),
                "avatar": avatarurl, "created": str(user.created)
                }
        message = temp
    else:
        message = "ERROR: Request method is not POST!"

    response = {"data": message}
    return HttpResponse(json.dumps(response), content_type='application/json')


def changeName(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body["email"]
        name = body["name"]

        updateDic = {"name": name}
        User.objects.filter(email=email).update(**updateDic)
        message = "Update Success"
    else:
        message = "ERROR: Request method is not POST!"

    response = {"data": message}
    return HttpResponse(json.dumps(response), content_type='application/json')


def changeAvatar(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        email = body["email"]
        url = str(body["avatar"])

        updateDic = {"avatarurl": url}
        User.objects.filter(email=email).update(**updateDic)
        message = "Update Avatar Success"
        code = 200
    else:
        message = "ERROR: Request method is not POST!"
        code = 404

    response = {"data": message, "code": code}
    return HttpResponse(json.dumps(response), content_type='application/json')


def checkAuth(request):
    request.encoding = 'utf-8'
    if 'commodityId' in request.GET and 'buyer' in request.GET and request.GET['commodityId'] and request.GET['buyer']:
        comm = Commodity.objects.filter(id=int(request.GET['commodityId'])).get()
        buyer = User.objects.filter(email=request.GET['buyer']).get()

        if comm.owner == buyer:
            # The owner can not post an offer to his own commodity
            message = False
        else:
            respond = Message.objects.filter(commodity=comm, buyer=buyer)
            if len(respond) > 0:
                # The buyer can not post one more offer to the same commodity
                message = False
            else:
                message = True

    else:
        message = "Query not submitted!"

    response = {"data": message}
    return HttpResponse(json.dumps(response), content_type='application/json')


def changePhone(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body["email"]
        phone = str(body["phone"])

        updateDic = {"phone": phone}
        User.objects.filter(email=email).update(**updateDic)
        message = "Update Phone Success"
        code = 200
    else:
        message = "ERROR: Request method is not POST!"
        code = 404

    response = {"data": message, "code": code}
    return HttpResponse(json.dumps(response), content_type='application/json')
