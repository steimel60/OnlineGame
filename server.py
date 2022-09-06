import socket
import threading
import sys
import pickle
from player import Player, playable_characters
from game import Game
from characters import CharacterSelector

#-------- Network Settings --------#
HEADER = 64
IP = "192.168.1.150"
port = 5555
FORMAT = 'utf-8'
DISCONNECT_MSG = "!Disconnect"

#------- Server Init -------#
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define connection type
try:
    server_socket.bind((IP,port))   #set up connection at given socket
except socket.error as e:
    print(e)



game = Game() #Initialize Game
colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255)]



def handle_client(conn, addr, player_id):
    """
    Handles communication between server and individual clients.
    """
    print(f"[NEW CONNECTION] {addr} connected.")
    #Send data for Client initialization
    send_client(conn, player_id) #send ID
    send_client(conn, game)                    #send game
    print("Start Connection")
    connected = True
    while connected:
        #Get data from client
        msg_len = conn.recv(HEADER).decode(FORMAT)  #Receive header from client
        if msg_len == None:
            break   #If connection broken break while loop
        msg_len = int(msg_len)                  #Str to int
        data = pickle.loads(conn.recv(msg_len)) #Load pickled data
        #Update Game
        if data == DISCONNECT_MSG:
            game.remove_player(player_id)
            connected = False
        elif isinstance(data, CharacterSelector):
            game.characters[data.name]['Selected'] = True
            game.players[player_id] = Player(playable_characters[data.name], player_id)

        elif isinstance(data, Player):
            game.update_player(data, player_id)
        #Send client updated game
        send_client(conn, game)
    conn.close()

def send_client(conn, data):
    """
    Sends header containing size of data in bytes. Then sends pickled data.
    """
    pkl = pickle.dumps(data) #pickle data
    msg_len = len(pkl)                          #Message length int
    send_len = str(msg_len).encode('utf-8')     #Message length in bytes
    send_len += b' ' * (HEADER - len(send_len)) #Add buffer
    conn.send(send_len) #Send length as header
    conn.send(pkl)      #Send data

def start():
    """
    Listen for connections and start threads.
    """
    player_id = 0
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept() #Wait for connection
        #On new connection create thread for client
        thread = threading.Thread(target=handle_client, args=(conn, addr, player_id))
        thread.start()
        #Add player to game
        player_id += 1
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

start()
