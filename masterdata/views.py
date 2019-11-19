from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'base.html',locals())


def maps(request):
    return render(request,'maps.html',locals())


    