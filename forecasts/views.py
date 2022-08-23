from django.shortcuts import render

# Create your views here.

def viewNetWorth(request):
    return render(request, "forecasts/net_worth.html")