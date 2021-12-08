from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import *


import json


# Form
def update_form(request):
    if 'query' in request.GET and request.GET['query']:
        id = int(request.GET['query'])
        typeNames = []
        for iType in CommodityType.objects.all():
            typeNames.append(iType.name)
    # TODO: Consider users with the same name

        return render(request, 'update_form.html', {"id": id, "typenames": typeNames})
    else:
        message = "ERROR: Request method is not POST!"
        return HttpResponse(message)


# Receive requested data to update certain commodities
def updateCommodity(request):
    if request.method == 'POST':
        # Used when connected with the 8080 frontend
        #
        body = json.loads(request.body)
        #
        # Also change "request.POST" in the following into "body"
        #
        id = int(body["id"])
        name = body["name"]
        description = body["description"]
        price = int(body["price"])
        onSale = True if body["onSale"] == "True" else False

        updateDic = {"name": name, "description": description, "price": price, "onsale": onSale}
        Commodity.objects.filter(id=id).update(**updateDic)
        # message = Commodity.objects.filter(name=name, description=description, category=category)
        message = "Commodity updated!"
    else:
        message = "ERROR: Request method is not POST!"

    response = {"data": message}
    return HttpResponse(json.dumps(response), content_type='application/json')
