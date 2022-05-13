"""This is for Board class set up"""

import pygame
import random 

class Board(object):
    ROWS = COLS = 90
    Colors = { 
        0: (255,255,255),
        1: (0,0,0),
        2: (255,0,0),
        3: (0,255,0),
        4: (0,0,255),
        5: (255,255,0),
        6: (255,140,0),
        7: (165,42,42),
        8: (128,0,128)
    }

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Width = 720
        self.Height = 720
        self.boardCompressed = []
        self.board = self.createBoard()
        self.borderThickness = 5

    def createBoard(self):
        return [[(255,255,255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def translateBoard(self):
        for y, _ in enumerate(self.boardCompressed):
            for x, col in enumerate(self.boardCompressed[y]):
                self.board[y][x] = self.Colors[col]

    def draw(self,win):
        pygame.draw.rect(win, (0, 0, 0), (self.x - self.borderThickness/2, self.y - self.borderThickness/2, self.Width + self.borderThickness, self.Height + self.borderThickness), self.borderThickness)
        for y, _ in enumerate(self.board):
            for x, col in enumerate(self.board[y]):
                pygame.draw.rect(win, col, (self.x + x*8, self.y + y*8, 8, 8), 0)

    def click(self,x,y):
        row = int((x - self.x)/8)
        col = int((y - self.y)/8)

        if 0 <= row <= self.ROWS and 0 <= col <=self.COLS:
            return row, col

        return None

    def update(self,x,y,color, thickness =3):
        nbr = [(x,y)] + self.neighborGetter(x,y)
        for x, y in nbr:
            if 0 <= x <= self.COLS and 0 <= y <= self.ROWS:
                self.board[y][x] = color

    def neighborGetter(self,x,y):
        return [ (x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

    def clear(self):
        self.board = self.createBoard()
