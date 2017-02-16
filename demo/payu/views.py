from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

from cart.forms import OrderForm, PayUForm, HashForm
from cart.utils import generate_hash, verify_hash

from django.contrib.webdesign.lorem_ipsum import sentence as lorem_ipsum
from uuid import uuid4
from random import randint
import logging

logger = logging.getLogger('django')

def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            initial = order_form.cleaned_data
            initial.update({'key': settings.PAYU_INFO['merchant_key'],
                            'surl': "http://surfly-dev.opentestdrive.com/order/success/",
                            'furl': "http://surfly-dev.opentestdrive.com/order/failure/",
                            'curl': "http://surfly-dev.opentestdrive.com/order/cancel/"})
            payu_form = PayUForm(initial)
            if payu_form.is_valid():                
                context = {'form': payu_form,
                           'hash_form':HashForm({'hash':generate_hash(payu_form.cleaned_data)}),
                           'action': settings.PAYU_INFO['payment_url']}
                return render(request, 'payu_form.html', context)
            else:
                logger.error('Something went wrong! Looks like initial data\
                        used for payu_form is failing validation')
                return HttpResponse(status=500)
    else:
        initial = {'txnid': uuid4().hex,
                'productinfo': "Description",
                'firstname': "Swagat",
                'email': "swagat@egrovesystems.com",
                'phone': "1234567890",
                'amount': randint(100, 1000)/100.0}
        order_form = OrderForm(initial=initial)
    context = {'form': order_form}
    return render(request, 'checkout.html', context)
 
 
@csrf_exempt
@require_POST
def success(request):
    if not verify_hash(request.POST):
        logger.warning("Response data for order (txnid: %s) has been "
                       "tampered. Confirm payment with PayU." %
                       request.POST.get('txnid'))
        return render(request, 'failure.html', {"res": request.POST})
    else:
        logger.warning("Payment for order (txnid: %s) succeeded at PayU" %
                       request.POST.get('txnid'))
        return render(request, 'success.html', {"res": request.POST})


@csrf_exempt
@require_POST
def failure(request):
    return render(request, 'failure.html', {"res": request.POST})


@csrf_exempt
@require_POST
def cancel(request):
    return render(request, 'cancel.html', {"res": request.POST})
