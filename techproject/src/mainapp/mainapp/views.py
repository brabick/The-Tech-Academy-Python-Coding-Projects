from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #format of a basic render
    products  = ['Cherries', 'Apples', 'Oranges', 'Strawberries', 'Pears', 'Watermelons']
    user = request.user
    context = {
        'products':products,

    }
    return render(request, 'home.html', context)