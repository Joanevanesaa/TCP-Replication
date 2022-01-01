import socket
import threading
from Player import player
host = socket.gethostname()
port = 8888

# membuat socket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((host, port)) #binding socket
ServerSocket.listen()
clients = [] #empty list for client
username = []
password = []

def handleClient(client, state):
    while True:
        try:
            #membaca input
            message = client.recv(5024)
            switchState(state, client)
            #Broadcast(message, client)
            #print(message)

        except:
            #remove client that is not related anymore
            clients.remove(client)
            client.close()

def switchState(number, client):
    switcher = {
        1: login(client),
        2: play(client),
        3: exit(client)
    }

def login(client):
    getUsername = client.send('Enter your username: '.encode('utf-8'))
    username = client.recv(1024)
    getPassword = client.send('Enter password: '.encode('utf-8'))
    password = client.recv(1024)
    newUser = player(username, password)

def play(client):
    playerStart = player.setPlay(True)
    client.send('Game start'.encode('utf-8'))

def exit(client):
    playerExit = player.setPlay(False)
    clients.remove(client)
    client.close()

def receive():
    while True:
        print('Server is running')
        client, address = ServerSocket.accept()
        print('Connected with: '+str(address))
        clients.append(client)

        client.send('Choose 1, 2, 3?'.encode('utf-8'))
        state = client.recv(1024)
        handleClient(client, state)

        client.send('you are now connected'.encode('utf-8'))
        thread = threading.Thread(target = handleClient, args=(client, ))
        thread.start()


if __name__ == "__main__":
    receive()