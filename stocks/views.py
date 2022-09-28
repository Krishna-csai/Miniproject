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

def gainers(request):
    return render(request, 'gainers.html')

def gainersfunction1(requets):
    gainers = nse.get_top_gainers()
    s = gainers[0]
    return JsonResponse(s, safe=False)

def gainersfunction2(requets):
    gainers = nse.get_top_gainers()
    s = gainers[1]
    return JsonResponse(s, safe=False)

def gainersfunction3(requets):
    gainers = nse.get_top_gainers()
    s = gainers[2]
    return JsonResponse(s, safe=False)

def losers(request):
    return render(request, 'losers.html')


def losersfunction1(requets):
    losers = nse.get_top_losers()
    s = losers[0]
    return JsonResponse(s, safe=False)

def losersfunction2(requets):
    losers = nse.get_top_losers()
    s = losers[1]
    return JsonResponse(s, safe=False)

def losersfunction3(requets):
    losers = nse.get_top_losers()
    s = losers[2]
    return JsonResponse(s, safe=False)