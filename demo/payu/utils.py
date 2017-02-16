from hashlib import sha512
from django.conf import settings
KEYS = ['key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10']

def generate_hash(data):
    hash = sha512('')
    hash_str = ''
    for key in KEYS:
        hash_str += "%s%s" % (str(data.get(key, '')), '|')
    hash_str += settings.PAYU_INFO.get('merchant_salt')
    print "hash_str = ", hash_str
    hash = sha512(hash_str)
    return hash.hexdigest().lower()

def verify_hash(data):
    keys = KEYS[:]
    keys.reverse()
    hash_str = ""
    hash = sha512(hash_str)
    hash_str += settings.PAYU_INFO.get('merchant_salt')
    hash_str += "%s%s" % ('|', str(data.get('status', '')))
    for key in keys:
        hash_str += "%s%s" % ('|', str(data.get(key, '')))
    hash.update(hash_str)
    return (hash.hexdigest().lower() == data.get('hash'))