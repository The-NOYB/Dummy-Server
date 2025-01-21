import socket
import threading

host = '127.0.0.1'
port = 7775

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
            received_info = client.recv(2048)
            received_obj = pickle.loads(info)
        except:
            client.close() 
            break

def main():
    while True:
        client, address = server.accept()

        client.send( "OBJ".encode('ascii') )
        player_object = pickle.loads(client.recv(2048))

        connected_clients.append(client)
        connected_objects.append(player_object)

        thread = threading.Thread( target=update_local, args=(client, ) )
        thread.start()
