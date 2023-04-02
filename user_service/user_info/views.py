# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import user_registration as userreg
# This function is for fetching the user data.


def user_data(uname):
    user = userreg.objects.filter(email=uname)
    for data in user.values():
        return data

# This function is created for getting the username and password.


@csrf_exempt
def user_info(request):
    resp = {}
    # uname = request.POST.get("User Name")
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            print(val1)
            uname = val1['uname']
            print(uname)
            if uname:
                # Calling the getting the user info.
                respdata = user_data(uname)
                print("checked:",respdata)
                dict1 = {}
                if respdata:
                    # dict1['fname'] = respdata.get('fname', '')
                    # dict1['lname'] = respdata.get('lname', '')
                    # dict1['mobile'] = respdata.get('mobile', '')
                    # dict1['email'] = respdata.get('email', '')
                    # dict1['address'] = respdata.get('address', '')
                    dict1['fname'] = respdata['fname']
                    dict1['lname'] = respdata['lname']
                    dict1['mobile'] = respdata['mobile']
                    dict1['email'] = respdata['email']
                    dict1['address'] = respdata['address']
                if dict1:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = dict1
                    # If a user is not found then it give failed as a response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
                    resp['data'] ={}
                    # The field value is missing.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
                resp['data'] ={}
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
            resp['data'] ={}
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
        resp['data'] ={}
    return HttpResponse(json.dumps(resp), content_type='application/json')
