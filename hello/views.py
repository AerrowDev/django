from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def aaron(request):
    return HttpResponse("Hello, Aaron. You're at the polls index.")

def john(request):
    return HttpResponse("Hello, John. You're at the polls index.")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
# HttpResponse(f"hello, {name.capitalize()}!")