""" This is for Board class set up """

class Board(object):
    ROWS = COLS = 90

    def __init__(self):
        self.data = self.emptyBoardSetup()

    def update(self,x,y,color):
        nbr = [(x, y)] + self.neighborGetter(x,y)
        for x, y in nbr:
            if 0 <= x <= self.COLS and 0 <= y <= self.ROWS:
                self.data[y][x] = color 
    
    def neighborGetter(self, x, y):
        return [ (x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

    def clear(self):
        self.data = self.emptyBoardSetup()

    def emptyBoardSetup(self):
        return [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
    
    def fill(self,x,y):
        pass

    def boardGetter(self):
        return self.data 