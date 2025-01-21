import socket
import threading

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect( ('127.0.0.1',7775) )

def receive():
    pass

def send():
