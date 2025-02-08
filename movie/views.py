from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   # return HttpResponse('<h1>Welcome to Home Page</h1>')
   #return render(request, 'movie/home.html')
   return render(request, 'home.html', {'name': 'Sofia Zapata'})

def about(request):
    # return HttpResponse('<h1>About Movies Review Page</h1><h2>Esta es la página About de mi sitio web</h2>')
    return render(request, 'about.html')