import socket
import threading
import pickle


class Network():
    def __init__(self):
        self.client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.host, self.port=  ('127.0.0.1',7776)
        
    # function will execute when client is launched and send the information of player on 1st connect
    def connect( self, player_obj ):
        try:
            self.client.connect( (self.host, self.port) )
            self.client.send( pickle.dumps(player_obj) )
        except socket.error as e:
            print(e)
        
    # fucntion will receive the data abotu all the other players
    def receive(self):
        try:
            pickle.loads( self.client.recv(2048*2) )
        except socket.error as e:
            print(e)
    
    # function will send data of player to the game
    def send(self):
        try:
            self.client.send( pickel.dumps(player_obj) )
        except socket.error as e:
            print(e)
