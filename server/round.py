"""This is for Round class set up"""

import time as t
from _thread import *
from chat import Chat 

class Round(object):
    def __init__(self,word,drawingPlayer,game):
        """
        initializing object 
        :param word:str
        :param drawingPlayer:player
        """
        self.word = word
        self.drawingPlayer = drawingPlayer
        self.guessPlayer = []
        self.skips = 0
        self.skippedPlayer = []
        self.game = game 
        self.chat = Chat(self)
        self.scoresPlayer = {player:0 for player in self.game.players}
        self.time = 75
        start_new_thread(self.timeThread, ())
    
    def timeThread(self):
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.endRound("Time's up!")
    
    def scoresGetter(self):
        return self.scoresPlayer

    def scoreGet(self, player):
        if player in self.scoresPlayer:
            return self.scoresPlayer[player]
        else:
            raise Exception("The player is not in score list.")

    def skip(self, player):
        if player not in self.skippedPlayer:
            self.skippedPlayer.append(player)
            self.skips += 1
            self.chat.chatUpdater(f"Player has voted to skip ({self.skips}/{len(self.game.players) - 2})")
            if self.skips >= len(self.game.players) - 2:
                return True

        return False 


    def guess(self,player,wrd):
        correct = wrd.lower() == self.word.lower()
        if correct:
            self.guessPlayer.append(player)
            #TODO implement scoring system here
            self.chat.chatUpdater(f"{player.name} has guessed the word.")
            return True
        self.chat.chatUpdater(f"{player.name} guessed {wrd}")

    def leftPlayer(self,player):
        if player in self.scoresPlayer:
            del self.scoresPlayer[player]
        if player in self.guessPlayer:
            self.guessPlayer.remove(player)
        if player == self.drawingPlayer:
            self.chat.chatUpdater("Round skipped due to the drawer leaving.")
            self.endRound("Drawing player leaves.")
    
    def endRound(self,msg):
        for player in self.game.players:
            if player in self.scoresPlayer:
                player.scoreUpdate(self.scoresPlayer[player])
        self.game.roundEnded()