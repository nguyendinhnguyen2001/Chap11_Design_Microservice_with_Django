# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
# from user_model.forms import UserForm
# from rest_framework.response import Response
from user_model.models import user_registration
from django.http import HttpResponse


def data_insert(fname, lname, email, mobile, password, address):
    user_data = user_registration(
        fname=fname, lname=lname, email=email, mobile=mobile, password=password, address=address)
    user_data.save()
    return 1


# def show_user(request):
#     if request.method == 'GET':
#         data = user_registration.objects.all()
#         serializer = UserForm(data, many=True)
#         return HttpResponse(serializer)


@csrf_exempt
def registration_req(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            user_register_data = json.loads(request.body)
            fname = user_register_data.get("fname")
            lname = user_register_data.get("lname")
            email = user_register_data.get("email")
            mobile = user_register_data.get("mobile")
            password1 = user_register_data.get("password1")
            password2 = user_register_data.get("password2")
            address = user_register_data.get("address")
            resp = {}
            print(fname)
            print(user_register_data)
            if fname and lname and email and mobile and password1 and password2 and address:

                if len(str(mobile)) == 10:
                    if password1 == password2:
                        respdata = data_insert(
                            fname, lname, email, mobile, password1, address)
                        if respdata:
                            resp['status'] = 'Success'
                            resp['status_code'] = '200'
                            resp['message'] = 'User is registered Successfully.'
                        else:
                            resp['status'] = 'Failed'
                            resp['status_code'] = '400'
                            resp['message'] = 'Unable to register user, Please try again.'
                    else:
                        resp['status'] = 'Failed'
                        resp['status_code'] = '400'
                        resp['message'] = 'Password and Confirm Password should be same.'

                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Mobile Number should be 10 digit.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
