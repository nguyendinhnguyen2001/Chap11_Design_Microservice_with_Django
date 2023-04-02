from django.shortcuts import render
import requests
import json
import datetime
from .models import Comment
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
# Create your views here.


def cmt_data_insert( email,product_id,comment):
    cmt_data = Comment(email = email,product_id = product_id, comment = comment,time_posted =datetime.datetime.now())
    cmt_data.save()
    return 1
# if val1['data']:
#             resp['First Name'] = val1['data']['fname']
#             resp['Last Name'] = val1['data']['lname']
#             resp['Mobile'] = val1['data']['mobile']
#             resp['Address'] = val1['data']['address']
#             resp['Email'] = val1['data']['email']

@api_view(['POST'])
def post_comment(request):
    uname = request.POST.get("User Name")
    product_id = request.POST.get('Product id')
    comment = request.POST.get('Comment')
    resp = {}

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
    
    url = 'http://127.0.0.1:8001/book/{}'.format(product_id)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    resp['products']=val1   

    respdata = cmt_data_insert(uname,product_id, comment)
    if respdata:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Post Comment Successfully'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed to Post Comment.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')  
@api_view(['GET'])
def get_comment(request,product_id):
      list_comment=Comment.objects.filter(product_id=product_id) 
      return Response({'data':list_comment,'message':'load success'})

  




