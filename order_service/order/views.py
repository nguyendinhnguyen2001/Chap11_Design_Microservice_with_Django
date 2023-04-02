import json
from django.shortcuts import render
import requests
import datetime
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order


@api_view(['POST'])
def get_order(request):
    uname=request.data.get('uname')
    url='http://127.0.0.1:8002/showcart/{}'.format(uname)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    check_remove=0
    if check_remove==0:
        for data in val1['products']:
            order=Order(cart_uname=uname,cart_product_id=data['product']['id'],cart_quantity=data['quantity'],cart_total=(float)(data['product']['price'])*data['quantity'],order_timeed=datetime.datetime.now())
            if order:
                order.save()
                check_remove=1
    if check_remove==1:        
        urls='http://127.0.0.1:8002/deletecart/{}'.format(uname)
        requests.delete(urls)
        return Response({'message': 'Success'})
    
    return Response({'message':'failed'})
     
