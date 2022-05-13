"""This is for Button class set up"""

import pygame 

class Button:
    def __init__(self, x, y, width, height, color, borderColor = (0, 0, 0)):
        self.x = x
        self.y = y
        self.height = height 
        self.width = width 
        self.color = color 
        self.borderColor = borderColor
        self.borderWidth = 2

    def draw(self,win):
        pygame.draw.rect(win, self.borderColor, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.color, (self.x + self.borderWidth, self.y + self.borderWidth,
        self.width - self.borderWidth*2, self.height - self.borderWidth*2), 0)

    def click(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height: 
            return True
        
        return False

class TextButton(Button):
    def __init__(self,x,y,width, height, color, text, borderColor= (0,0,0)):
        super().__init__(x,y,width,height,color,borderColor)
        self.text = text 
        self.textFont = pygame.font.SysFont("comicsans", 30)

    def changeFontSize(self,size):
        self.textFont = pygame.font.SysFont("comicsans", size)\
    
    def draw(self,win):
        super().draw(win)
        txt = self.textFont.render(self.text, 1, (0,0,0))
        win.blit(txt, (self.x + self.width/2 - txt.get_width()/2,self.y+ self.height/2 - txt.get_height()/2))