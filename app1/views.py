from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def drinks(request):
    return HttpResponse('drink here')