# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from payment.models import payment_status
from shipment_update.views import shipment_details_update as ship_update
# This function is for fetching the user data.


def get_transaction_details(uname):
    user = payment_status.objects.filter(username=uname)
    for data in user.values():
        return data
# This function is used for storing the data.


def store_data(uname, prodid, price, quantity, mode_of_payment, mobile):
    user_data = payment_status(username=uname, product_id=prodid, price=price, quantity=quantity,
                               mode_of_payment=mode_of_payment, mobile=mobile, status="Success")
    user_data.save()
    return 1
# This function is created for getting the payment.

# {
#   "User Name":"nguyen@gmail.com",
#   "Product id":"1",
#   "Product price":"159000",
#   "Product quantity":"1",
#   "Payment mode":"success",
#   "Mobile Number":"0541269732"
# }


@csrf_exempt
def get_payment(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get("User Name")
            prodid = val1.get("Product id")
            price = val1.get("Product price")
            quantity = val1.get("Product quantity")
            mode_of_payment = val1.get("Payment mode")
            mobile = val1.get("Mobile Number")

            resp = {}
            if uname and prodid and price and quantity and mode_of_payment and mobile:
                print(uname)
                # It will call the store data function.
                respdata = store_data(uname, prodid, price,
                                      quantity, mode_of_payment, mobile)
                print(respdata)
                # respdata2 = ship_update(uname)
                # If it returns value then will show success.
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'Transaction is completed.'
                # If it is returning null value then it will show failed.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Transaction is failed, Please try again.'
            # If any mandatory field is missing then it will be through a failed message.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'
            return HttpResponse(json.dumps(resp), content_type='application/json')
# This function is created for getting the username and password.


@csrf_exempt
def user_transaction_info(request):
    # uname = request.POST.get("User Name")
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('User Name')
            resp = {}
            if uname:
                # Calling the getting the user info.
                respdata = get_transaction_details(uname)
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = respdata
                # If a user is not found then it give failed as response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
            # The field value is missing.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
