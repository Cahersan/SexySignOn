from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    token = request.META['HTTP_SSO_UUID']
    token_uuid = token.split(":")[1]

    return HttpResponse("UUID is %s" % token_uuid)
