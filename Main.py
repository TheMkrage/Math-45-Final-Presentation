import Board
from Board import Board

# size of board and then 
board = Board(10, 0.0)
board.print()
board.nextTurn()

print(board.getValue(5, 6))