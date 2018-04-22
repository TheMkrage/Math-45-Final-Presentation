import random
import threading


class Board:
    
    def __init__(self, dimension=40, probability=0.1, fighters=1):
        print("init")
        self.dimension = dimension
        self.probability = probability/4.0
        self.fighters = fighters
        self.map = [[0 for j in range(self.dimension)] for i in range(self.dimension)]
        col = int(len(self.map)/2)
        row = int(len(self.map[0])/2)
        for i in range(5):
            for j in range(5):
                self.map[col-2+i][row-3+j] = 1
        self.turn = 0


    def __repr__(self):
        out = ""
        for i in range(len(self.map)):
            out += (str(self.map[i]) + "\n")
        return out

    def print(self):
        for i in range(len(self.map)):
            print(self.map[i])
    
    def spreadFireIfNecessary(self, col, row):
        # Make sure there is a valid place to spread to
        #MAYBE !=0
        if col >= 0 and col < self.dimension and row < self.dimension and row >= 0 and self.map[col][row]!=1:
            if random.random() < self.probability:
                return (col, row)
        return None

    def nextTurn(self):
        print("Next Turn, Turn#: "+str(self.turn))
        spacesToChangeToFire = []
        spacesFought = []
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
                self.map[pair[0]][pair[1]] = 1
        for col in range(self.dimension-1):
            for row in range(self.dimension-1):
                if (self.map[col][row]==1) and (self.countNeighbors(col,row)<8):
                    spacesFought.append((col,row))
        random.shuffle(spacesFought)
        for pair in spacesFought[:10*self.fighters]:
                self.map[pair[0]][pair[1]] = 0
        self.turn += 1


    def getValue(self, col, row):
        return self.map[col][row]

    def change1(self,col,row):
        self.map[col][row] = 1
    
    def countNeighbors(self, row,col):
        count = 0
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if self.map[r][c] == 1: 
                    count = count+1
        if self.map[row][col]==1: count = count -1
        return count