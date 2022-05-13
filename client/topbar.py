"""This is for Top Bar class set up"""

import pygame

class topBar(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width 
        self.height = height 
        self.word = ""
        self.round = 1
        self.maxRound = 8 
        self.roundFont = pygame.font.SysFont("comicsans", 50)
        self.borderThickness = 5
        self.time = 75 
        self.drawing = False 
    
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.width, self.height), self.borderThickness)
        txt = self.roundFont.render(f"Round {self.round} of {self.maxRound}", 1, (0,0,0))
        win.blit(txt, (self.x + 10, self.y + self.height/2 - txt.get_height()/2))

        if self.drawing:
            wd = self.word
        else:
            wd = topBar.underscoreText(self.word)
        txt = self.roundFont.render(wd, 1, (0,0,0))
        win.blit(txt, (self.x + self.width/2 - txt.get_width()/2, self.y + self.height/2 - txt.get_height()/2 + 10))

        pygame.draw.circle(win, (0,0,0), (self.x + self.width - 50, self.y + round(self.height/2)), 40, self.borderThickness)

        timer = self.roundFont.render(str(self.time), 1, (0,0,0))

        win.blit(timer, (self.x + self.width - 50 - timer.get_width()/2, self.y + self.height/2 - timer.get_height()/2))
    
    @staticmethod
    def underscoreText(text):
        newStr = ""

        for char in text: 
            if char != " ":
                newStr += " _ "
            else:
                newStr += "  "
        return newStr
    def wordChanger(self, word):
        self.word = word 
    def roundChanger(self, rd):
        self.round = rd