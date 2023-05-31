from django.http import HttpResponse
from django.shortcuts import render
import datetime
def test(request):
    date = datetime.datetime.now()
    print("test function is called from view")
    return HttpResponse("<h1>hello this is index page</h1>"+ " "+str(date))

def about(request):
    print("test function is called from view")
    #return HttpResponse("<h1>hello this is about page</h1>")
    return render(request,"about.html",{})

def home(request):
    date = datetime.datetime.now()
    
    isActive = True
    name = "Vikash Kumar"
    
    

    Data ={
        'date': date,
        'isActive' : isActive,
        'name' : name,
    }
    
    print("test function is called from view")
    #return HttpResponse("<h1>hello this is home page</h1>")
    return render(request,"home.html",Data)

def services(request):
    print("test function is called from view")
    #return HttpResponse("<h1>hello this is services page</h1>")
    return render(request,"services.html",{})

