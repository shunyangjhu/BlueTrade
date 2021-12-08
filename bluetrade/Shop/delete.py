from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import *
import json


# Form
def deleteCommodity(request):
    if 'query' in request.GET and request.GET['query']:
        id = int(request.GET['query'])

        Commodity.objects.filter(id=id).delete()

        message = "Commodity deleted!"
    else:
        message = "ERROR: Request method is not GET!"
    return HttpResponse(message)


def deleteCommodityPost(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        id = int(body["id"])
        Commodity.objects.filter(id=id).delete()

        message = "Commodity deleted!"
    else:
        message = "ERROR: Request method is not POST!"

    response = {"data": message}
    return HttpResponse(json.dumps(response), content_type='application/json')
