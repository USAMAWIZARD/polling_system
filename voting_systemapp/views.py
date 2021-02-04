from django.shortcuts import render,redirect
import json

voters={}
candidate={}
votes=[]
# Create your views here.

  
def home(request):
    return render(request,'index.html')

def registervoter(request):
    voters[request.POST["email"]]={"name":request.POST["username"],"gender":request.POST["gender"],"age":request.POST["age"],"voted":0}
    return redirect('/allcandidates/')
def registercandidate(request):
    candidate[request.POST["name"]]={"partyname":request.POST["partyname"],"age":request.POST["age"],"votes":0}
    return redirect('/allcandidates/')

def allcandidates(request):
    print(candidate)
    return render(request,"allcandidates.html",{"candidates":candidate})
