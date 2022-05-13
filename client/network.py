"""This is for Network class set up"""

import socket
import json
import time as t 

class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.105.98.201"
        self.port = 5556
        self.addr = (self.server, self.port)
        self.name = name 
        self.connect()
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode())
            s = ""
            while 1:
                last = self.client.recv(1024).decode()
                s += last 
                try:
                    if s.count(".") == 1:
                        break
                except:
                    pass
            
            try:
                if s[-1] == ".":
                    s = s[:-1]
            except:
                pass

            keys = [key for key in data.keys()]
            return json.loads(s)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)
    
    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server.", msg)
        self.client.close()