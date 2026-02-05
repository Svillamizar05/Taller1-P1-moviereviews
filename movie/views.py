from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Welcome to the Movie Reviews Home Page<h1>')
    return render(request, 'home.html', {'name': 'Santehhh'})   
