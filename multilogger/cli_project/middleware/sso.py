from django.shortcuts import render
from django.http import HttpResponse
import hmac
import hashlib
import base64

# Create your views here.
class SSOCheck(object):

    def process_request(self, request):
        key = 'this is a very secret key!'
        token = request.META['HTTP_SSO_UUID']

        token_uuid = token.split(":")[1]
        token_hmac = token.split(":")[0]
        
        digest = hmac.new(key.encode('utf-8'), token_uuid.encode('utf-8'), hashlib.sha1).digest()
        generated_hmac = base64.b64encode(digest).decode('utf-8')
        
        if token_hmac != generated_hmac:
            return HttpResponse("Tampering detected")
