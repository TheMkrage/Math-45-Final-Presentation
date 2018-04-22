# Name: Kyle Grace


import Board
from Board import *
import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(dim, prob, fighters):
    """ returns a 2d array with "height" rows and "width" cols """
    board = Board(dim,prob, fighters)
    return board

def printBoard(A):
    """ this function prints the 2d list-of-lists A
    """
    A.print()

def next_life_generation(A):
    """ makes a copy of A and then advances one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
        """
    return A.nextTurn()