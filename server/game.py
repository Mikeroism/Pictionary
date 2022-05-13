"""This is for Game class set up"""

import random
from board import Board 
from round import Round

class Game(object):
    def __init__(self,id,players):
        self.id=id
        self.players = players
        self.round= None
        self.usedWords = set()
        self.board = Board()
        self.drawingPlayerIndex = 0
        self.roundCount = 1
        self.newRoundStarter()
    

    def guessedPlayer(self,player,guess):
        return self.round.guess(player, guess)
    
    def playerScoresGetter(self):
        scores = {player.name:player.scoreGetter() for player in self.players}
        return scores 

    def disconnctedPlayer(self,player):
        if player in self.players:
            self.players.remove(player)
            self.round.leftPlayer(player)
            self.round.chat.chatUpdater(f"Player {player.nameGetter()} disconnected.")
        else:
            raise Exception("Player not in the game.")

        if len(self.players) <= 2:
            self.gameEnded()

    def skip(self, player):
        if self.round:
            newRound = self.round.skip(player)
            if newRound:
                self.round.chat.chatUpdater(f"Round skipped.")
                self.roundEnded()
                return True
            return False 

        else:
            raise Exception("No round has been started.")

    def roundEnded(self):
        self.round.chat.chatUpdater(f"Round {self.roundCount} has ended.")
        self.newRoundStarter()
        self.board.clear()

    def newRoundStarter(self):
        try:
            self.round = Round(self.wordGetter(), self.players[self.drawingPlayerIndex],self)
            self.roundCount += 1
            
            if self.drawingPlayerIndex >= len(self.players):
                self.roundEnded()
                self.gameEnded()

            self.drawingPlayerIndex += 1

        except Exception as e:
            self.gameEnded()
    

    def updateBoard(self,x,y,color):
        if not self.board:
            raise Exception("No board has been created.")
        self.board.update(x,y,color)

    def wordGetter(self):
        with open("words.txt", "r") as f:
            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in self.usedWords:
                    words.append(wrd)

        wrd = random.choice(words)
        self.usedWords.add(wrd)

        return wrd
    
    def gameEnded(self):
        print(f"[GAME] Game {self.id} ended.")
        for player in self.players:
            player.game = None 
