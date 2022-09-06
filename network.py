import socket
import pickle

class Network:
    def __init__(self):
        #Set up connection to server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_IP = "192.168.1.150"
        self.port = 5555
        self.addr = (self.server_IP, self.port)
        self.connect()
        self.header_size = 64
        #Store player data
        self.player_id = self.get()
        self.player = None

    def get_player(self):
        return self.player

    def get_id(self):
        return self.player_id

    def set_player(self, player):
        self.player = player

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            print("Could not connect to server.")

    def send(self, data):
        pkl = pickle.dumps(data)
        msg_len = len(pkl)                                    #Message length int
        send_len = str(msg_len).encode('utf-8')               #Message length in bytes
        send_len += b' ' * (self.header_size - len(send_len)) #Add buffer
        self.client.send(send_len) #Send length as header
        self.client.send(pkl)      #Send data

    def get(self):
        #Get data from client
        msg_len = self.client.recv(self.header_size).decode('utf-8')  #Receive header from client
        if msg_len != None:
            msg_len = int(msg_len) #Str to int
            return pickle.loads(self.client.recv(msg_len)) #Load data
