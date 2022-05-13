"""This is for Leaderboard class set up"""

import pygame

class Leaderboard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 200
        self.HEIGHT_ENTRY = 80
        self.players = []
        self.nameFont = pygame.font.SysFont("comicsans", 25, bold = True)
        self.scoreFont = pygame.font.SysFont("comicsans", 20)
        self.rankFont = pygame.font.SysFont("comiscans", 60)
        self.borderThickness = 5 
    
    def draw(self,win):
        scores = [ ( player.name, player.score) for player in self.players]
        scores.sort(key = lambda x : x[1], reverse = True )

        for i, score in enumerate(scores):
            if i % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (200, 200, 200)
            pygame.draw.rect(win, color, (self.x, self.y + i*self.HEIGHT_ENTRY, self.WIDTH, self.HEIGHT_ENTRY))

            rank = self.rankFont.render("#" + str(i+1), 1, (0,0,0))
            win.blit(rank, (self.x + 10, self.y + i*self.HEIGHT_ENTRY + self.HEIGHT_ENTRY/2 - rank.get_height()/2 ) )
            name = self.nameFont.render(score[0], 1, (0,0,0))
            win.blit(name, (self.x - name.get_width()/2 + self.WIDTH/2, self.y + i*self.HEIGHT_ENTRY + 20)) 
            score = self.scoreFont.render("Score:" + str(score[1]), 1, (0,0,0))
            win.blit(score, (self.x - name.get_width()/2 + self.WIDTH, self.y + i*self.HEIGHT_ENTRY + 40))
        
        pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.WIDTH, self.HEIGHT_ENTRY * len(scores)), self.borderThickness)
    
    def addPlayer(self,player):
        self.players.append(player)

    def removePlayer(self,player):
        self.players.remove(player)
