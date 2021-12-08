from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

import json
from collections import defaultdict
import random


from .models import *

# Form
def search_form(request):
    return render(request, 'search_form.html')


# Receive requested data to search certain commodities
def searchCommodity(request):
    request.encoding = 'utf-8'
    if 'searchQuery' in request.GET and request.GET['searchQuery']:
        query = request.GET['searchQuery']
        commoditySet = Commodity.objects.filter(Q(name__icontains=query)
                                                | Q(category__icontains=query)
                                                | Q(description__icontains=query))
    else:
        commoditySet = Commodity.objects.all()

    if len(commoditySet) > 0:
        # message = defaultdict(list)
        message = []
        idx = 0
        for comm in commoditySet:
            if comm.completed == 1:
                # Omit those traded commodities
                continue

            photos = []
            if comm.url != "":
                photos = comm.url.split()

            temp = {"id": str(comm.id), "name": comm.name, "owner": comm.owner.name,
                    "category": comm.category, "description": comm.description, "price": str(comm.price),
                    "num of stock": str(comm.numofstock), "created": str(comm.createdate), 
                    "updateDate": str(comm.updatedate)[:10],
                    "photos": photos}
            # message[idx] = temp
            message.append(temp)
            idx += 1
    else:
        message = "Commodity Not found!"

    response = {"data": message}
    return HttpResponse(json.dumps(response), content_type='application/json')


def search_id_form(request):
    return render(request, 'search_id.html')


def searchById(request):
    request.encoding = 'utf-8'
    if 'commodityId' in request.GET and request.GET['commodityId']:
        id = int(request.GET['commodityId'])
        commoditySet = Commodity.objects.filter(id=id)
        if len(commoditySet) > 0:
            comm = commoditySet.get()
            photos = []
            if comm.url != "":
                photos = comm.url.split()

            message = {"id": str(comm.id),
                       "name": comm.name, "owner": comm.owner.name,
                       "category": comm.category,
                       "description": comm.description,
                       "price": str(comm.price), "numofstock": str(comm.numofstock),
                       "createDate": str(comm.createdate), "updateDate": str(comm.updatedate)[:10],
                       "onSale": comm.onsale, "photos": photos}
        else:
            message = "Commodity Not found!"
    else:
        message = "Query Not Submitted!"

    response = {"data": message}
    return HttpResponse(json.dumps(response), content_type='application/json')


def searchByOwner(request):
    request.encoding = 'utf-8'
    if 'owner' in request.GET and request.GET['owner']:
        owner = User.objects.filter(email=request.GET['owner']).get()
        commoditySet = Commodity.objects.filter(owner=owner)
        if len(commoditySet) > 0:
            # message = defaultdict(list)
            message = []
            idx = 0
            for comm in commoditySet:
                temp = {"id": str(comm.id),
                        "name": comm.name, "owner": comm.owner.name, "category": comm.category,
                        "description": comm.description, "price": str(comm.price),
                        "num of stock": str(comm.numofstock), "createDate": str(comm.createdate),
                        "updateDate": str(comm.updatedate)[:10], "onSale": True}
                # message[idx] = temp
                message.append(temp)
                idx += 1
        else:
            message = "Commodity Not found!"
            message = []
    else:
        message = "Query Not Submitted!"

    response = {"data": message}

    return HttpResponse(json.dumps(response), content_type='application/json')


def recommend(request):
    request.encoding = 'utf-8'
    if 'email' in request.GET and request.GET['email']:
        user = User.objects.filter(email=request.GET['email']).get()
        commoditySet = Commodity.objects.filter(onsale=True)
        message = []
        if len(commoditySet) > 0:
            idx = 0
            for comm in commoditySet:
                if idx >= 6:
                    break
                if random.random() > 0.5:
                    continue

                photos = []
                if comm.url != "":
                    photos = comm.url.split()

                temp = {"id": str(comm.id), "name": comm.name, "owner": comm.owner.name,
                        "category": comm.category, "description": comm.description, "price": str(comm.price),
                        "num of stock": str(comm.numofstock), "createDate": str(comm.createdate),
                        "updateDate": str(comm.updatedate)[:10],
                        "photos": photos}
                # message[idx] = temp
                message.append(temp)
                idx += 1

    else:
        message = "Query not Submitted!"

    response = {"recommendations": message}
    return HttpResponse(json.dumps(response), content_type='application/json')