from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import *

import json


# Form
def post_form(request):
    userNames = []
    for iUser in User.objects.all():
        userNames.append(iUser.name)

    # typeNames = []
    # for iType in CommodityType.objects.all():
    #     typeNames.append(iType.name)

    # TODO: Consider users with the same name

    # return render(request, 'post_form.html', {"usernames": userNames, "typenames": typeNames})
    return render(request, 'post_form.html', {"usernames": userNames})


# Receive requested data to create certain commodities
def postTest(request):
    if request.method == 'POST':
        # Used when connected with the 8080 frontend
        #
        # body = json.loads(request.body)
        #
        # Also change "request.POST" in the following into "body"
        #
        name = request.POST["name"]
        owner = User.objects.filter(name=request.POST["owner"]).get()
        # type = CommodityType.objects.filter(name=request.POST["type"]).get()
        description = request.POST["description"]
        price = int(request.POST["price"])
        category = request.POST["category"]
        numofstock = int(request.POST["numofstock"])
        onsale = True if request.POST["onsale"] == "True" else False

        postDic = {"name": name, "owner": owner, "description": description,
                   "price": price, "category": category, "numofstock": numofstock,
                   "onsale": onsale}
        Commodity.objects.create(**postDic)
        # message = Commodity.objects.filter(name=name, description=description, category=category)
        message = "Commodity posted!"
    else:
        message = "ERROR: Request method is not POST!"
    return HttpResponse(message)


# Receive requested data to create certain commodities
def postCommodity(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        name = body["name"]
        owner = User.objects.filter(email=body["owner"]).get()
        description = body["description"]
        price = int(body["price"])
        category = body["category"]

        urls = body["photos"]
        store_url = ""
        for url in urls:
            store_url += url
            store_url += " "

        postDic = {"name": name, "owner": owner,
                   "description": description, "price": price, "category": category, "numofstock": 1,
                   "onsale": True, "url": store_url}

        Commodity.objects.create(**postDic)
        # _post_image_url(urls, commodity.commodityid)
        # message = Commodity.objects.filter(name=name, description=description, category=category)
        message = "Commodity posted!"
    else:
        message = "ERROR: Request method is not POST!"

    response = {"data": message, "code": 200}
    return HttpResponse(json.dumps(response), content_type='application/json')

