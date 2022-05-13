"""This is for Game class set up"""

import pygame 
from board import Board
from button import Button, TextButton 
from leaderboard import Leaderboard
from player import Player
from topbar import topBar 
from bottombar import bottomBar
from chat import Chat
from network import Network

class Game:
    Bg = (255, 255, 255)
    COLORS = {
        (255, 255, 255): 0,
        (0, 0, 0): 1,
        (255, 0, 0): 2,
        (0, 255, 0): 3,
        (0, 0, 255): 4,
        (255, 255, 0): 5,
        (255, 140, 0): 6,
        (165, 42, 42): 7,
        (128, 0, 128): 8
    }

    def __init__(self, win, connection = None):
        pygame.font.init()
        self.connection = connection
        self.win = win
        self.leaderboard = Leaderboard(50, 125)
        self.board = Board(305, 125)
        self.topbar = topBar(10, 10, 1280, 100)
        self.topbar.roundChanger(1)
        self.players = []
        self.skipButton = TextButton(85,830,125,60,(255,255,0), "Skip")
        self.bottombar = bottomBar(305, 880, self)
        self.chat = Chat(1050,125)
        self.drawColor = (0,0,0)
        self.drawing = False

    def addPlayer(self, player):
        self.players.append(player)
        self.leaderboard.addPlayer(player)

    def draw(self):
        self.win.fill(self.Bg)
        self.leaderboard.draw(self.win)
        self.topbar.draw(self.win)
        self.board.draw(self.win)
        self.skipButton.draw(self.win)
        if self.drawing:
            self.bottombar.draw(self.win)
        self.chat.draw(self.win)
        pygame.display.update()

    def checkClick(self):
        mose = pygame.mose.getPosition()

        if self.skipButton.click(*mose) and not self.drawing:
            skips = self.connection.send({1:[]})


        boardClicked = self.board.click(*mose)

        if boardClicked:
            self.board.update(*boardClicked, self.drawColor)
            self.connection.send({8:[*boardClicked, self.COLORS[tuple(self.drawColor)]]})

    def run(self):
        r = True 
        clk = pygame.time.Clock()
        while r:
            clk.tick(60)
            try:
                response = self.connection.send({3:[]})
                if response:
                    self.board.boardCompressed = response
                    self.board.translateBoard()

                response = self.connection.send({9: []})
                self.topbar.time = response

                response = self.connection.send({2: []})
                self.chat.updateChat(response)

                self.topbar.word = self.connection.send({6: []})
                self.topbar.round = self.connection.send({5: []})
                self.drawing = self.connection.send({11: []})
                self.topbar.drawing = self.drawing
                self.topbar.maxRound = len(self.players)

                '''response = self.connection.send({0:[]})
                self.players = []
                for player in response:
                    p = Player(player)
                    self.addPlayer(p)'''

            except:
                r = False
                break

            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
                    break

                if pygame.mose.getPressed()[0]:
                    self.checkClick()
                    self.bottombar.buttonEvent()

                if event.type == pygame.KEYDOWN:
                    if not self.drawing:
                        if event.key == pygame.K_RETURN:
                            self.connection.send({0: [self.chat.typing]})
                            self.chat.typing = ""
                        else:
                            keyName = pygame.key.name(event.key)
                            keyName = keyName.lower()
                            self.chat.type(keyName)

        pygame.quit()


