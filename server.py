import socket
import pickle
import threading
from player import Player_data

host = '127.0.0.1'
port = 7777

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server.bind( (host, port) )
server.listen()

connected_clients = []  # list of all connected clients
connected_objects = []  # list of all player objects
other_objects = []      # other objects which are not dependent on clients

# sending the changes to the clients/players
def edit_obj(connected_objects, received_obj):
    for obj in connected_objects:
        if obj.name == received_obj.name:
            obj.update( received_obj )

# function for updating the changes on server
def update(client, connected_clients, connected_objects):
    while True:
        try:
            index = connected_clients.index(client) 
            received_obj = pickle.loads( client.recv(2048*2) )
            client.send( pickle.dumps(connected_objects) )
            edit_obj( connected_objects, received_obj)
        except:
            print(f"{connected_objects[index].name} has disconnected to the server")
            connected_clients.pop( index )
            connected_objects.pop( index )
            print( connected_clients, connected_objects)
            client.close() 
            break

def main():
    print("Server has started")

    while True:
        client, address = server.accept()
        player_object = pickle.loads(client.recv(2048*2))

        # this was for getting the player object initially
#        client.send( "OBJ".encode('ascii') )

        connected_clients.append(client)
        connected_objects.append(player_object)

        print(f"{player_object.name} has connected to the server with {address = }")
        # will work on this later
#        client.send( "You're now connected to the server".encode('ascii') )

        thread = threading.Thread( target=update, args=(client, connected_clients, connected_objects,) )
        thread.start()

main()
