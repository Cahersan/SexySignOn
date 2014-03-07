import hashlib
import hmac
import time

def hmac_sha1_token():
    timestamp = str(time.time())
    hmac_pass = hmac.new(b'some very secret string', timestamp.encode('utf-8'), hashlib.sha1).hexdigest()
    token = '%s:%s' % (timestamp, hmac_pass)
    return token 

