import json
from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer

# ship_dict = {}
#     # It is used for getting data from payment info.
#     user = paystat.objects.filter(username=uname)
#     for data in user.values():
#         data
#     ship_dict['Product Id'] = data['product_id']
#     ship_dict['Quantity'] = data['quantity']
#     ship_dict['Payment Status'] = data['status']
#     ship_dict['Transaction Id'] = data['id']
#     ship_dict['Mobile Number'] = data['mobile']
#     # It is used for getting the user info.
#     url = 'http://127.0.0.1:8000/userinfo/'
#     d1 = {}
#     d1["User Name"] = data['username']
#     data = json.dumps(d1)
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, data=data, headers=headers)
#     val1 = json.loads(response.content.decode('utf-8'))
#     ship_dict['First Name'] = val1['data']['First Name']
#     ship_dict['Last Name'] = val1['data']['Last Name']
#     ship_dict['Address'] = val1['data']['Address']
#     ship_dict['Email Id'] = val1['data']['Email Id']
@api_view(['GET'])
def show_cart(request,uname):

    if request.method == 'GET':  # user requesting data
        resp={}
        listcart = Cart.objects.filter(uname=uname)
        # serializer = CartSerializer(listcart, many=True)
        url = 'http://127.0.0.1:8000/userinfo/'
        d1 = {}
        d1["uname"] = uname
        data = json.dumps(d1)
        print(data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        val1 = json.loads(response.content.decode('utf-8'))
        print(val1)
        if val1['data']:
            resp['First Name'] = val1['data']['fname']
            resp['Last Name'] = val1['data']['lname']
            resp['Mobile'] = val1['data']['mobile']
            resp['Address'] = val1['data']['address']
            resp['Email'] = val1['data']['email']
        list_product=[]
        for cart in listcart:
            url = 'http://127.0.0.1:8001/book/{}'.format(cart.product_id)
            headers = {'Content-Type': 'application/json'}
            response = requests.get(url, headers=headers)
            val1 = json.loads(response.content.decode('utf-8'))
            list_product.append({'product':val1,'quantity':cart.quantity})
        resp['products']=list_product
        return Response(resp)#headers = {'Content-Type': 'application/json'}
@api_view(['POST'])
def add_cart( request):
    if request.method == 'POST':  # user posting data
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request,uname):
    if request.method == 'DELETE':
        cart_remove=Cart.objects.filter(uname=uname)
        for cart in cart_remove:
            cart.delete()
        return Response({"status":"success","product":cart_remove}, status=status.HTTP_204_NO_CONTENT)