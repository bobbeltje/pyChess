
import pandas as pd
import modules.pieces as cp
from modules.utils import *

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]
        

def start_game() :
    
    global FILES, RANKS
    
    board = pd.DataFrame([[0]*8]*8)
    board.columns = FILES
    board.index = RANKS
    
    #def get_available_moves(self, board, pos, col) :
    p1 = cp.Pawn('white')
    p2 = cp.Pawn('black')
    
    moves = p1.get_available_moves(board, ('e', 2))
    print(moves)
    moves = p2.get_available_moves(board, ('e', 7))
    print(moves)
    moves = p2.get_available_moves(board, ('f', 5))
    print(moves)

if __name__ == '__main__' :
    
    start_game()
