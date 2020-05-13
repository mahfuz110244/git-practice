from django.shortcuts import render, HttpResponse


# Create your views here.
def Home(request):
    print(request)
    print("Home Page View")
    return HttpResponse("Home Page")
