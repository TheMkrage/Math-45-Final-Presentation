# by Obosa Obazuaye, HMC '14: Summer 2011

# make sure this is implemented!
from Diffeq_Modeler import next_life_generation

import time
from turtle import *
import csgrid; from csgrid import *
from random import *

import Board
from Board import *

# summary of keypresses:
print("  PAUSE: 'p'")
print(" RESUME: 'Return'/'Enter'")
print("  RESET: 'Space'")
print("  CLOSE: 'Esc'")
print()
print("Start with start() ...")
print()

# the function to start:
def start(dimension = 50, probability = 0.5, fighters = 1):
    # start-up turtle stuff
    reset()  # clear the screen
    tracer(False) # turn off turtle animation
    delay(0)  # go as fast as possible
    global board, screen
    screen = Screen()
    board = Board(dimension, probability, fighters)
    screen.listen()
    onscreenclick(lifeMouseHandler)
    screen.onkey(showgood2, "Return")
    screen.onkey(bye, "Escape")
    screen.onkey(blank, "space")
    show(board)
    done()


global board

def allOnes(L):
    """Checks if the board is all ones"""
    if type(L) != list:
        L = L.map
    counter = 0
    for List in L:
        if List == [1]*len(List): counter+=1
    return counter == len(L)

def allZeroes(L):
    if type(L) != list:
        L = L.map
    counter = 0
    for List in L:
        if List == [0]*len(List): counter+=1
    return counter == len(L)
    
def showgood():
    """Makes the next life generation appear"""
    global board
    board.nextTurn
    show(board)

running = True
def showgood2():
    """Sets the board to keep moving through generations of life.
        Allows for pausing with "p", resuming with "Enter"/"Return",
        and automatically pauses the game if the board stops changing
        or becomes blank."""
    global board
    global running
    screen.onkey(gamepause, "p")
    screen.onkey(gameresume, "Return")
    screen.listen()
    if running:
        if (board == next_life_generation(board) == next_life_generation(next_life_generation(board))):
            print(str(board.turn) + " hours to stabilize!")
            showgood()
            running = False
        elif allOnes(board):
            print(str(board.turn) + " hours to consume full board!")
            showgood()
            running = False
        elif allZeroes(board):
            print(str(board.turn) + " hours before we stopped the fire!")
            showgood()
            running = False
        else:
            showgood()
            screen.ontimer(showgood2, t=0)
            #The t value above sets how many milliseconds there are
            # between each generation of life. Set it low (e.g. 0 seconds, or 500
            # for half a second, etc.) for fast movement, or
            # set it high (e.g. 1000 for 1 second, 3000 for 3 seconds, etc.)
            # for fast slower movement.

def gamepause():
    """Pauses the game"""
    global running
    running = False

def gameresume():
    """Resumes a paused game."""
    global running
    running = True
    showgood2()
    
def blank():
    """Makes the board blank (resets the board)"""
    global board
    board = createBoard(board.dimension,board.probability,board.fighters) # of zeros
    show(board)

def createBoard(dimension,probability,fighters):
    """ returns a 2d array of width and height """
    board = Board(dimension, probability, fighters)
    return board




    
