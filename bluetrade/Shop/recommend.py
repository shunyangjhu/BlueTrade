from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

import json
from collections import defaultdict


from .models import *


def recommendCommodity(request):
    allTypes = CommodityType.objects.all()
    typeList = [type.name for type in allTypes]
    numOfTypes = len(typeList)
    typeWeight = [0.4, 0.2, 0.2, 0.2]
    numOfCommodity = 5
    numOfEach = [int(weight*numOfCommodity) for weight in typeWeight]
    # Adding items into list
    message = defaultdict(list)
    idx = 0
    for i in range(numOfTypes):
        upperBound = numOfEach[i]
        type = CommodityType.objects.filter(name=typeList[i]).get()
        commoditySet = Commodity.objects.filter(type=type)
        # Control the number of items in each type
        cnt = 0
        for comm in commoditySet:
            if cnt == upperBound:
                break
            cnt += 1
            temp = [str(comm.id),
                    comm.name, comm.owner.name, comm.type.name,
                    comm.category, comm.description, str(comm.price),
                    str(comm.numofstock), str(comm.created), str(comm.updated)]
            message[idx] = temp
            idx += 1

    return HttpResponse(json.dumps(message), content_type='application/json')

