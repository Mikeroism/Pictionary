"""This is for Chat class set up"""

import pygame

class Chat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 225
        self.HEIGHT = 800
        self.borderThickness = 5
        self.content = []
        self.typing = ""
        self.chatFont = pygame.font.SysFont("comicsans", 20)
        self.typeFont = pygame.font.SysFont("comicsans", 30)
        self.chatGap = 20

    def updateChat(self, content):
        self.content = content 

    def draw(self, win):
        pygame.draw.rect(win, (200, 200, 200), (self.x, self.y + self.HEIGHT - 40, self.WIDTH, 40))
        pygame.draw.line(win, (0, 0, 0), (self.x, self.y + self.HEIGHT - 40), (self.x + self.WIDTH, self.y + self.HEIGHT - 40), self.borderThickness)
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.WIDTH, self.HEIGHT), self.borderThickness)

        while len(self.content) * self.chatGap > self.HEIGHT - 60:
            self.content = self.content[:-1]

        for a, chat in enumerate(self.content):
            txt = self.chatFont.render("-" + chat, 1, (0, 0, 0))
            win.blit(txt, (self.x + 8, 10 + self.y + a*self.chatGap))

        typeChat = self.typeFont.render(self.typing, 1, (0, 0, 0))
        win.blit(typeChat, (self.x + 5, self.y + self.HEIGHT - 17 - typeChat.get_height()/2))

    def type(self, charac):
        if charac == "backspace":
            if len(self.typing) > 0:
                self.typing = self.typing[:-1]
        elif charac == "space":
            self.typing += " "
        elif len(charac) == 1:
            self.typing += charac 

        if len(self.typing) >= 25:
            self.typing = self.typing[:25]