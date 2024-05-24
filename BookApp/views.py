from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .serializers import booksSerializers
from rest_framework.request import Request
from rest_framework.decorators import api_view,throttle_classes,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


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
    rate = '500/day'

@api_view(['GET', 'POST'])
@throttle_classes([OncePerDayUserThrottle])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
# @permission_classes([])
# @permission_classes([IsAdminUser])
def form1(request:Request, version=None):
    
    if request.method == "POST":
        form = booksSerializers(data = request.data)
            
        if form.is_valid():
            form.save()
            return Response("Thanks..........", status=201)
        else :
            return Response({"error":form.errors},status=400)
    else:
        Bookdata = Books2.objects.all()
        form = booksSerializers(Bookdata, many=True)
        

    # return render(request, "form.html", {"form": form})
    return Response({"message":"Hello all", "data": form.data}, status=200)


@api_view(['GET','PUT'])
def form2(request:Request,id):
    try :
        data1 = Books2.objects.get(pk=id)
        form = booksSerializers(data1,request.data,partial=True)
        if form.is_valid():
            form.save()
            return Response({"ans":form.data},status=200)
        else :
            return Response(form.errors,status=400)
    except :
        return Response("data does not exist!",status=404)