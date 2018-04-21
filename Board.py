import random
import threading

class Board:
    
    def __init__(self, dimension, probability):
        print("init")
        self.dimension = dimension
        self.probability = probability
        self.map = [[False for j in range(self.dimension)] for i in range(self.dimension)]
        col = int(len(self.map)/2)
        row = int(len(self.map[0])/2)
        self.map[col][row] = True

    def print(self):
        for i in range(len(self.map)):
            print(self.map[i])
    
    def spreadFireIfNecessary(self, col, row):
        # Make sure there is a valid place to spread to
        if col >= 0 and col < self.dimension and row < self.dimension and row >= 0 and not self.map[col][row]:
            if random.random() < self.probability:
                return (col, row)
        return None

    def nextTurn(self):
        print("Next Turn")
        spacesToChangeToFire = []
        for col in range(self.dimension):
            for row in range(self.dimension):
                if self.map[col][row]:
                    if self.spreadFireIfNecessary(col - 1, row) != None:
                        spacesToChangeToFire.append((col - 1, row))
                    if self.spreadFireIfNecessary(col + 1, row) != None:
                        spacesToChangeToFire.append((col + 1, row))
                    if self.spreadFireIfNecessary(col, row - 1) != None:
                        spacesToChangeToFire.append((col, row - 1))
                    if self.spreadFireIfNecessary(col, row + 1) != None:
                        spacesToChangeToFire.append((col, row + 1))
        for pair in spacesToChangeToFire:
            self.map[pair[0]][pair[1]] = True
        self.print()

    def getValue(self, col, row):
        return self.map[col][row]
