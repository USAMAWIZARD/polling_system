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
    print(request.POST["email"])
    return render(request,"allcandidates.html",{"candidates":candidate,"emailid":request.POST["email"]})

def registercandidate(request):
    candidate[request.POST["name"]]={"partyname":request.POST["partyname"],"age":request.POST["age"],"votes":0}
    return redirect('/allcandidates/')

def allcandidates(request):
    print(candidate)
    return render(request,"allcandidates.html",{"candidates":candidate})

async def websocket_applciation(scope, receive, send):
    while True:
        event = await receive()
        print(scope)
        print(" new connn")
        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })

        if event['type'] == 'websocket.disconnect':
            break
            
        if event['type'] == 'websocket.receive':
            print("hlow")
            eventdata=json.loads(event['text'])
            print(eventdata)
            function= list(eventdata.keys())[0]
            if function=="addvote":
                if  voters[eventdata["addvote"]["email"]]["voted"]:
                    candidate[eventdata["addvote"]["tovote"]]["votes"]+=1
                    voters[eventdata["addvote"]["email"]]["voted"]=True
                    await send({
                        'type': 'websocket.broadcast',
                        'text': eventdata["addvote"]["tovote"]
                    })                  
                else:
                    await send({
                        'type': 'websocket.broadcast',
                        'text': 'already voted'
                    })