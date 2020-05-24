from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse(request, "home.html")
    return render(request, 'home.html')

def contact(request):
    #return HttpResponse(request, "home.html")
    context = {
        'namber': 123,
        'name': 'aleksander',
        'list': [1,2,3,4,5,6,7,'abc']
    }
    return render(request, 'contact.html', context)    