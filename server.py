import socket
import pickle
import threading
from player import Player

host = '127.0.0.1'
port = 7776

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server.bind( (host, port) )
server.listen()

connected_clients = []  # list of all connected clients
connected_objects = []  # list of all player objects
other_objects = []      # other objects which are not dependent on clients

# sending the changes to the clients/players
def broadcast():
    pass

# function for updating the changes on server
def update_local(client):
    while True:
        try:
            received_info = client.recv(2048*2)
            received_obj = pickle.loads(info)
        except:
            index = connected_clients.index(client) 
            print(f"{connected_objects[index].name} has disconnected to the server")
            connected_clients.pop( index )
            connected_objects.pop( index )
            client.close() 
            break

def main():
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

        thread = threading.Thread( target=update_local, args=(client, ) )
        thread.start()

main()
