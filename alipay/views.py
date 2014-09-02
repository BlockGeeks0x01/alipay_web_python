# Create your views here.

import requests

from django.http import HttpResponseRedirect

from models import Order
from utils import create_direct_pay_by_user
from utils import GATE_WAY


def alipay(request):
    user_name = 'harrison'
    try:
        order = Order.get(user_name=user_name)
    except:
        order = Order.objects.create(user_name=user_name, status=0)

    order_num = order.pk

    return HttpResponseRedirect(create_direct_pay_by_user(order_num, 'cake', 0.01))