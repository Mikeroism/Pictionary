"""This is for Main Menu class set up"""

import pygame 
from game import Game 
from network import Network 
from player import Player 

class mainMenu:
    Bg= (255, 255, 255)
    def __init__(self):
        self.WIDTH  = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.name = ""
        self.waiting = False 
        self.nameFont = pygame.font.SysFont("comicsans", 80)
        self.titleFont = pygame.font.SysFont("comicsans", 120)
        self.enterFont = pygame.font.SysFont("comicsans", 60)

    def draw(self):
        self.win.fill(self.Bg)
        title = self.titleFont.render("Pictionary", 1, (0,0,0))
        self.win.blit(title,  (self.WIDTH/2 - title.get_width()/2, 50) ) 

        name = self.nameFont.render("Type a name:" + self.name, 1, (0,0,0))
        self.win.blit(name, (100, 400))

        if self.waiting:
            enter = self.enterFont.render("In queue.....", 1, (0,0,0))
            self.win.blit(enter, (self.WIDTH/2 - title.get_width() / 2, 800))
        else:
            enter = self.enterFont.render("Press enter to join the game:", 1, (0,0,0))
            self.win.blit(enter, (self.WIDTH/2 - title.get_width()/2, 800))
        
        pygame.display.update()
    
    def run(self):
        r = True 
        clk = pygame.time.Clock()
        while r:
            clk.tick(30)
            self.draw()
            if self.waiting:
                response = self.n.send({-1:[]})
                if response:
                    r = False
                    g = Game(self.win, self.n)

                    for player in response:
                        p = Player(player)
                        g.addPlayer(p)
                    g.run()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.name) > 1:
                            self.waiting = True 
                            self.n = Network(self.name)
                    else:
                        keyName = pygame.key.name(event.key)

                        keyName = keyName.lower()
                        self.type(keyName)
    
    def type(self, charac):
        if charac == "backspace":
            if len(self.name) > 0:
                self.name = self.name[:-1]
        elif charac == "space":
            self.name += " "
        elif len(charac) == 1:
            self.name += charac 
        
        if len(self.name) >= 20:
            self.name = self.name[:20]

if __name__ == "__main__":
    pygame.font.init()
    main = mainMenu()
    main.run()
