from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from nsetools import Nse
nse = Nse()
import requests
# Create your views here.
def home(request):
    return render(request, 'homepage.html')
        
def codes(request):
    return render(request, 'codes.html')

def codesfunction(request):
    codes = nse.get_stock_codes()
    return JsonResponse(codes, safe=False)

def searchpage(request, code):
    s = nse.get_quote(code)
    return JsonResponse(s, safe=False)

def search(request):
    return render(request, 'search.html')

def credits(request):
    return render(request, 'credits.html')