"""This is for Handler class class set up"""

import threading
import socket 
import json
from player import Player 
from game import Game 

class Server(object):
    NumOfPlayers = 4 

    def __init__(self):
        self.connectionQueue = []
        self.gameId = 0

    def playerThread(self,conn,player):
        while True:
            try:
                try:
                    data = conn.recv(1024)
                    data = json.loads(data.decode())
                except Exception as e:
                    break 

                keys = [int(key) for key in data.keys()]
                sendMsg = {key:[] for key in keys}
                lastBoard = None 

                for key in keys:
                    if key == -1: 
                        if player.game:
                            send = {player.nameGetter():player.scoreGetter() for player in player.game.players}
                            sendMsg[-1] = send
                        else:
                            sendMsg[-1] = []
                    
                    if player.game:
                        if key == 0:
                            correct = player.game.guessedPlayer(player, data['0'][0])
                            sendMsg[0] = correct 
                        elif key == 1:
                            skip = player.game.skip(player)
                            sendMsg[1] = skip 
                        elif key == 2:
                            displayedOutput = player.game.round.chat.chatGetter()
                            sendMsg[2] = displayedOutput
                        elif key == 3:
                            brd = player.game.board.boardGetter()
                            if lastBoard != brd:
                                lastBoard = brd
                                sendMsg[3] = brd
                        elif key == 4:
                            scores = player.game.playerScoresGetter()
                            sendMsg[4] = scores 
                        elif key == 5:
                            rnd = player.game.roundCnt 
                            sendMsg[5] = rnd
                        elif key == 6:
                            word = player.game.round.word
                            sendMsg[6] = word
                        elif key == 7:
                            skp = player.game.round.skips 
                            sendMsg[7] = skp
                        elif key == 8:
                            if player.game.round.drawingPlayer == player:
                                x,y,color = data['8'][:3]
                                player.game.updateBoard(x,y,color)
                        elif key == 9:
                            t1 = player.game.round.time 
                            sendMsg[9] = t1
                        elif key == 10:
                            player.game.board.clear()
                        elif key == 11:
                            sendMsg[11] = player.game.round.drawingPlayer == player

                sendMsg = json.dumps(sendMsg)
                conn.sendall(sendMsg.encode() + ".".encode())
            except Exception as e:
                print(f"[EXCEPTION] {player.nameGetter()}:", e)
                break

        if player.game:
            player.game.disconnectedPlayer(player)

        if player in self.connectionQueue:
            self.connectionQueue.remove(player)
        
        print(F"[DISCONNECT] {player.name} DISCONNECTED.")
        conn.close()
    
    def handleQueue(self,player):
        self.connectionQueue.append(player)

        if len(self.connectionQueue) >= self.NumOfPlayers:
            game1 = Game(self.gameId, self.connectionQueue[:])
            for p in game1.players:
                p.gameSetter(game1)
            
            self.gameId += 1
            self.connectionQueue =[]
            print(f"[GAME] Game {self.gameId -1} has started.")
        
    def authentication(self,conn, addr):
        try:
            data = conn.recv(1024) 
            name = str(data.decode())
            if not name:
                raise Exception("No name has been received.")
            conn.sendall("1".encode())

            player1 = Player(addr, name)
            self.handleQueue(player1)
            thread = threading.Thread(target = self.playerThread, args=(conn,player1))
            thread.start()
        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()
    
    def connectionThread(self):
        server = ""
        port = 5556

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen(1) 
        print("Server has been started, connection waiting...")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New connection.")

            self.authentication(conn,addr)
    
if __name__ == "__main__":
    s = Server()
    thread = threading.Thread(target = s.connectionThread)
    thread.start()