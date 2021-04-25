import asyncio 
import websockets
import json
from voting_systemapp import views
connected =list()


async def websocketrequest(websocket, path):
    eventdata=""

    if websocket not in connected: 
        connected.append(websocket) 

    async for message in websocket:
        eventdata = json.loads(message)
        print(eventdata)
        function = list(eventdata.keys())[0]
        if function == "addvote": 
            if not views.readJSON("voter")[eventdata["addvote"]["email"]]["voted"]:
                towrite=views.readJSON("candidatae")
                towrite[eventdata["addvote"]["tovote"]]["votes"] += 1
                views.writeJSON("candidatae",towrite)

                #voters[eventdata["addvote"]["email"]]["voted"] = True
                # brodcaste voted 
                print(len(connected))
                print(eventdata["addvote"]["tovote"])
                for conn in connected:
                    try:     
                        await conn.send(eventdata["addvote"]["tovote"])
                    except:
                        pass
                        # Unregister
                        #connected.remove(websocket)
            else:
                pass
                # already voted

asyncio.get_event_loop().run_until_complete(
websockets.serve(websocketrequest, 'localhost', 3000))
asyncio.get_event_loop().run_forever()


