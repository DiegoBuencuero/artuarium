from django.shortcuts import render

def index(request):
    return render (request, "index.html")

def about(request):
    return render (request, "about.html")

def services(request):
    return render (request, "services.html")

def starter(request):
    return render (request, "starter.html")


def contact(request):
    pass

def thanks(request):
    pass




