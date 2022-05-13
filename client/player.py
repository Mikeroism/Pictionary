"""This is for Player class set up"""

class Player(object):
    def __init__(self, name):
        self.name = name 
        self.score = 0
    
    def scoreUpdate(self, x):
        self.score += x 

    def scoreGetter(self):
        return self.score
    
    def nameGetter(self):
        return self.name