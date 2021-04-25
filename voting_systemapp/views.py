from django.shortcuts import render, redirect
import json
import  json
import asyncio

voters = {}
candidate = {}

def readJSON(filename):
    with open(filename+'.json') as f:
        data = json.load(f)
    return data

def writeJSON(filename,data):
    with open(filename+'.json', 'w') as f:
        json.dump(data, f)


def home(request):
    return render(request, 'index.html')

def registervoter(request):

    voters[request.POST["email"]]={"name":request.POST["username"],"gender":request.POST["gender"],"age":request.POST["age"],"adharnumber":request.POST["adharno"],"pancardno":request.POST["pancardno"],"voterid":request.POST["voterid"],"voted":False}
    print(request.POST["email"])
    writeJSON("voter",voters)
    return render(request,"allcandidates.html",{"candidates":readJSON("candidatae"),"emailid":request.POST["email"]})


def registercandidate(request):
    print(request.POST["partyname"])
    candidate[request.POST["name"]]={"partyname":request.POST["partyname"],"age":request.POST["age"],"votes":0}
    writeJSON('candidatae',candidate)
    return redirect('/allcandidates/')


def allcandidates(request):
    return render(request,"allcandidates.html",{"candidates":readJSON("candidatae")})








