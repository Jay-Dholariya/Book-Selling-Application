from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import booksform
from rest_framework.request import Request
from rest_framework.decorators import api_view,throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle


# Create your views here.

# def  home(request):  ///this is for create a variable and its render in html template 
    # name = Author.objects.filter(firstname='Tulsi').values_list("firstname")
    # 
    
    # context={'firstname':'jay'}
    # return render (request,'index.html',context)
    
    # firstname = 'jay'
    # return render(request,'index.html',{'firstname':firstname})
    
def demo(request):
    mymember = Author.objects.all().values()
    return render(request,"index.html",{'member':mymember})

def testing(request):
    context = {'heading': "the hello &lt; heyy &gt; byy < heyy"}
    return render(request,'test.html',context)

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '5/day'

@api_view(['GET', 'POST','DELETE'])
@throttle_classes([OncePerDayUserThrottle])
def form1(request:Request):
    if request.method == "POST":
        form = booksform(request.POST)
            
        if form.is_valid():
            form.save()
            return Response("Thanks..........")
    else:
        form = booksform()

    # return render(request, "form.html", {"form": form})
    return Response({"message":"Hello all"})