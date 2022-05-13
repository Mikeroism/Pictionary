"""This is for Player class set up """

from .game import Game 

class Player(object): 
    def __init__(self,ip,name):
        self.ip = ip
        self.game = None
        self.name = name
        self.score = 0

    def scoreUpdate(self, x):
        self.score += x
    
    def gameSetter(self,game):
        self.game = game 

    def guess(self, wrd):
        return self.game.guessedPlayer(self, wrd)

    def disconnect(self):
        self.game.diconnectedPlayer(self)

    def scoreGetter(self):
        return self.score

    def nameGetter(self):
        return self.name
    
    def ipGetter(self):
        return self.ip