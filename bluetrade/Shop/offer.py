from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail

from .models import *

import json


# Form
def offer_form(request):
    userIDs = []
    for iUser in User.objects.all():
        userIDs.append(iUser.id)

    commodityIDs = []
    for iComm in Commodity.objects.all():
        commodityIDs.append(iComm.id)

    return render(request, 'offer_form.html', {"userIDs": userIDs, "commodityIDs": commodityIDs})


def offerCommodity(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        # price = int(request.POST["price"])
        # message = request.POST["message"]
        # buyer = User.objects.filter(id=int(request.POST["buyer"])).get()
        # commodity = Commodity.objects.filter(id=int(request.POST["commodity"])).get()
        price = int(body["price"])
        message = body["message"]
        buyer = User.objects.filter(email=body["buyer"]).get()
        # buyer = User.objects.filter(id=int(body["buyer"])).get()
        commodity = Commodity.objects.filter(id=int(body["commodityId"])).get()
        # 0 indicating "just posted", 1 indicating "confirmed"
        status = 0

        postDic = {"price": price, "message": message, "buyer": buyer,
                   "commodity": commodity, "status": status}
        Message.objects.create(**postDic)

        respond = "Offer posted! Email has been sent to the seller: "
        respond += commodity.owner.email

        emailContent = 'You have received an offer.'
        targetList = [commodity.owner.email]
        send_mail(subject='Django Test', message=emailContent,
                  from_email=None, recipient_list=targetList,
                  fail_silently=False)

    else:
        respond = "ERROR: Request method is not POST!"

    response = {"data": respond}
    return HttpResponse(json.dumps(response), content_type='application/json')


def offerConfirmation(request):
    request.encoding = 'utf-8'
    if 'query' in request.GET and request.GET['query']:
        bid = Message.objects.filter(id=int(request.GET['query']))
        bid = bid[0]
        if bid.status == 1:
            respond = "This bid has already been confirmed!"
        elif bid.commodity.completed == 1:
            respond = "This commodity has already been traded!"
        else:
            updateDic = {"status": 1}
            Message.objects.filter(id=bid.id).update(**updateDic)

            updateDic = {"selectedbuyer": bid.buyer.name, "completed": 1}
            Commodity.objects.filter(id=bid.commodity.id).update(**updateDic)

            respond = "Trade Confirmed! Email has been sent to the buyer: "
            respond += bid.buyer.email
            respond += '\nName of the commodity: '
            respond += str(bid.commodity.name)
            respond += '\nWith price: '
            respond += str(bid.price)

            emailContent = 'You offer has been confirmed.'
            emailContent += '\nName of the commodity: '
            emailContent += str(bid.commodity.name)
            emailContent += '\nWith price: '
            emailContent += str(bid.price)
            targetList = [bid.buyer.email]
            send_mail(subject='Django Test', message=emailContent,
                      from_email=None, recipient_list=targetList,
                      fail_silently=False)

    else:
        respond = "Query Not Submitted!"

    return HttpResponse(respond)


def offerByCommodityID(request):
    request.encoding = 'utf-8'
    if 'query' in request.GET and request.GET['query']:
        commodity = Commodity.objects.filter(id=int(request.GET['query'])).get()
        offerSet = Message.objects.filter(commodity=commodity)
        if len(offerSet) > 0:
            respond = []
            idx = 0
            for offer in offerSet:
                temp = {"id": str(offer.id), "price": str(offer.price), "message": offer.message,
                        "buyer": offer.buyer.name, "commodity": offer.commodity.name,
                        "created": str(offer.created), "status": str(offer.status)}
                respond.append(temp)
                idx += 1
        else:
            respond = "Offer Not found!"
    else:
        respond = "Query Not Submitted!"
    return HttpResponse(json.dumps(respond), content_type='application/json')


def offerByBuyerID(request):
    request.encoding = 'utf-8'
    if 'query' in request.GET and request.GET['query']:
        buyer = User.objects.filter(id=int(request.GET['query'])).get()
        offerSet = Message.objects.filter(buyer=buyer)
        if len(offerSet) > 0:
            respond = []
            idx = 0
            for offer in offerSet:
                temp = {"id": str(offer.id), "price": str(offer.price), "message": offer.message,
                        "buyer": offer.buyer.name, "commodity": offer.commodity.name,
                        "created": str(offer.created), "status": str(offer.status)}
                respond.append(temp)
                idx += 1
        else:
            respond = "Offer Not found!"
    else:
        respond = "Query Not Submitted!"

    response = {"data": respond}
    return HttpResponse(json.dumps(response), content_type='application/json')


def offerByBuyerEmail(request):
    request.encoding = 'utf-8'
    if 'owner' in request.GET and request.GET['owner']:
        buyer = User.objects.filter(email=request.GET['owner']).get()
        offerSet = Message.objects.filter(buyer=buyer)
        if len(offerSet) > 0:
            respond = []
            idx = 0
            for offer in offerSet:
                temp = {"id": str(offer.id), "price": str(offer.price), "message": offer.message,
                        "buyer": offer.buyer.name, "commodity": offer.commodity.name,
                        "created": str(offer.created), "status": str(offer.status)}
                respond.append(temp)
                idx += 1
        else:
            respond = "Offer Not found!"
    else:
        respond = "Query Not Submitted!"

    response = {"data": respond}
    return HttpResponse(json.dumps(response), content_type='application/json')


def offerStillBuying(request):
    request.encoding = 'utf-8'
    if 'buyer' in request.GET and request.GET['buyer']:
        buyer = User.objects.filter(email=request.GET['buyer']).get()

        highestPrice = 0
        offerSet = Message.objects.all()
        for offer in offerSet:
            highestPrice = max(highestPrice, offer.price)

        # offerSet = Message.objects.filter(buyer=buyer, status=0)
        offerSet = Message.objects.filter(buyer=buyer)
        if len(offerSet) > 0:
            respond = []
            idx = 0
            for offer in offerSet:
                if offer.status == 3 or offer.status == 4:
                    continue
                temp = {"id": str(offer.id), "price": str(offer.price), "message": offer.message,
                        "buyer": offer.buyer.name, "commodityName": offer.commodity.name,
                        "created": str(offer.created), "status": offer.status,
                        "highestPrice": str(highestPrice)}
                respond.append(temp)
                idx += 1
        else:
            respond = "Offer Not found!"
    else:
        respond = "Query Not Submitted!"

    response = {"data": respond}
    return HttpResponse(json.dumps(response), content_type='application/json')


def offerStillSelling(request):
    request.encoding = 'utf-8'
    if 'commodityId' in request.GET and request.GET['commodityId']:
        comm = Commodity.objects.filter(id=int(request.GET['commodityId'])).get()
        # offerSet = Message.objects.filter(commodity=comm, status=0)
        offerSet = Message.objects.filter(commodity=comm)
        print(offerSet)
        if len(offerSet) > 0:
            respond = []
            idx = 0
            for offer in offerSet:
                if offer.status == 3 or offer.status == 4:
                    continue
                temp = {"id": str(offer.id), "price": str(offer.price), "message": offer.message,
                        "buyerName": offer.buyer.name, "commodityName": offer.commodity.name,
                        "created": str(offer.created), "status": offer.status,
                        "email": offer.buyer.email}
                respond.append(temp)
                idx += 1
        else:
            respond = "Offer Not found!"
    else:
        respond = "Query Not Submitted!"

    response = {"data": respond}
    return HttpResponse(json.dumps(response), content_type='application/json')


def offerCompleted(request):
    request.encoding = 'utf-8'
    if 'consumer' in request.GET and request.GET['consumer']:
        consumer = User.objects.filter(email=request.GET['consumer']).get()

        offerSet = Message.objects.filter(buyer=consumer, status=3)
        respond1 = []
        if len(offerSet) > 0:
            idx = 0
            for offer in offerSet:
                temp = {"id": str(offer.id), "price": str(offer.price), "message": offer.message,
                        "buyer": offer.buyer.name, "commodityName": offer.commodity.name,
                        "created": str(offer.created), "status": offer.status}
                respond1.append(temp)
                idx += 1

        commoditySet = Commodity.objects.filter(owner=consumer)
        respond2 = []
        if len(commoditySet) > 0:
            for comm in commoditySet:
                offerSet = Message.objects.filter(commodity=comm, status=3)
                for offer in offerSet:
                    temp = {"id": str(offer.id), "price": str(offer.price), "message": offer.message,
                            "buyer": offer.buyer.name, "name": offer.commodity.name,
                            "created": str(offer.created), "status": offer.status}
                    respond2.append(temp)

        response = {"data": {"buyer": respond1, "seller": respond2}}

    else:
        respond = "Query Not Submitted!"
        response = {"data": respond, "code": 404}

    return HttpResponse(json.dumps(response), content_type='application/json')


def offerCommodityUpdate(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        # price = int(request.POST["price"])
        # message = request.POST["message"]
        # buyer = User.objects.filter(id=int(request.POST["buyer"])).get()
        # commodity = Commodity.objects.filter(id=int(request.POST["commodity"])).get()
        price = int(body["price"])
        message = body["message"]
        buyer = User.objects.filter(email=body["email"]).get()
        # commodity = Commodity.objects.filter(id=int(body["commodityId"])).get()

        bid = Message.objects.filter(id=int(body["commodityId"])).get()


        updateDic = {"price": price, "message": message}
        Message.objects.filter(buyer=buyer, id=int(body["commodityId"])).update(**updateDic)

        respond = "Offer updated! Email has been sent to the seller: "
        respond += bid.commodity.owner.email

        emailContent = 'You have received an offer.'
        targetList = [bid.commodity.owner.email]
        send_mail(subject='Django Test', message=emailContent,
                  from_email=None, recipient_list=targetList,
                  fail_silently=False)
        code = 200

    else:
        respond = "ERROR: Request method is not POST!"
        code = 404

    response = {"data": respond, "code": code}
    return HttpResponse(json.dumps(response), content_type='application/json')


def offerConfirmationPost(request):
    if request.method == 'POST':
        body = json.loads(request.body)


        buyer = User.objects.filter(email=body["email"]).get()

        bid = Message.objects.filter(id=body["commodityId"], buyer=buyer).get()
        comm = bid.commodity

        # Not selecting any other bid
        otherBids = Message.objects.filter(commodity=comm)
        for other in otherBids:
            if other.buyer != buyer:
                updateDic = {"status": 2}
                Message.objects.filter(id=other.id).update(**updateDic)


        if bid.status == 1:
            respond = "This bid has already been confirmed!"
        elif bid.commodity.completed == 1:
            respond = "This commodity has already been traded!"
        else:
            updateDic = {"status": 1}
            Message.objects.filter(id=bid.id).update(**updateDic)

            # updateDic = {"selectedbuyer": bid.buyer.name, "completed": 1, "onsale": False}
            # Commodity.objects.filter(id=bid.commodity.id).update(**updateDic)

            respond = "Trade Confirmed! Email has been sent to the buyer: "
            respond += bid.buyer.email
            respond += '\nName of the commodity: '
            respond += str(bid.commodity.name)
            respond += '\nWith price: '
            respond += str(bid.price)

            emailContent = 'You offer has been confirmed.'
            emailContent += '\nName of the commodity: '
            emailContent += str(bid.commodity.name)
            emailContent += '\nWith price: '
            emailContent += str(bid.price)
            targetList = [bid.buyer.email]
            send_mail(subject='Django Test', message=emailContent,
                      from_email=None, recipient_list=targetList,
                      fail_silently=False)

        code = 200
    else:
        respond = "Query Not Submitted!"
        code = 404

    response = {"data": respond, "code": code}
    return HttpResponse(json.dumps(response), content_type='application/json')


def offerComplete(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        # print(body)

        buyer = body["buyer"]
        price = body["price"]
        id = body["commodityId"]
        name = body["name"]

        bid = Message.objects.filter(id=id).get()
        comm = bid.commodity

        # Not selecting any other bid
        otherBids = Message.objects.filter(commodity=comm)
        for other in otherBids:
            if other.buyer != buyer:
                updateDic = {"status": 4}
                Message.objects.filter(id=other.id).update(**updateDic)

        updateDic = {"status": 3}
        Message.objects.filter(id=bid.id).update(**updateDic)

        updateDic = {"selectedbuyer": bid.buyer.email, "completed": 1, "onsale": False}
        Commodity.objects.filter(id=bid.commodity.id).update(**updateDic)

        respond = "Confirmed!"
        code = 200

    else:
        respond = "Query Not Submitted!"
        code = 404

    response = {"data": respond, "code": code}
    return HttpResponse(json.dumps(response), content_type='application/json')
