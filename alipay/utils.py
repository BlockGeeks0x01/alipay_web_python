__author__ = 'harrison'
from hashlib import md5
from urllib import urlencode

GATE_WAY = 'https://mapi.alipay.com/gateway.do?'

def create_direct_pay_by_user(tn, subject, total_fee):
    params = dict()
    params.update({
        "service": "create_direct_pay_by_user",
        "partner": "2088901729140845",
        "_input_charset": "utf-8",
        "notify_url": "http://www.xxx.com/create_direct_pay_by_user/notify",
        "return_url": "http://www.xxx.com/create_direct_pay_by_user/return_url",
        ########
        "out_trade_no": str(tn),
        "subject": subject,
        "payment_type": '1',
        "total_fee": total_fee,
        "seller_id": "2088901729140845",
        "seller_email": "abcx@123feng.com"
    })
    params, prestr = params_filter(params)
    params['sign'] = sign(prestr, 'lvmiz8fk49m69d4r8akg4g5xmq18esnx', 'MD5')
    params['sign_type'] = 'MD5'

    return GATE_WAY + urlencode(params)


def params_filter(params):
    ks = params.keys()
    ks.sort()
    new_params = dict()
    prestr = ''
    for k in ks:
        v = params[k]
        if v and k not in ('sign', 'sign_type'):
            new_params[k] = v
            prestr += '%s=%s&' % (k, new_params[k])
    prestr = prestr[:-1]

    print new_params
    return new_params, prestr


def sign(prestr, key, sign_type='MD5'):
    if sign_type == 'MD5':
        return md5(prestr+key).hexdigest()
    else:
        return ''