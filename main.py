
import pandas as pd
import modules.pieces as cp
from modules.utils import *

# Note that the indeces of FILES & RANKS go from 0 to 7
FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]

# Note consider using two dictionaries to hold the positions        

def start_game() :
    
    global FILES, RANKS
    
    board = pd.DataFrame([[0]*8]*8)
    board.columns = FILES
    board.index = RANKS
    
    for i in range(8) :
        board[FILES[i]].loc[7] = cp.Pawn('black')
        board[FILES[i]].loc[2] = cp.Pawn('white')

    # pawn trials
    '''
    p1 = cp.Pawn('white')
    p2 = cp.Pawn('black')
    p3 = cp.Pawn('white')
    p3.enpassant = 'f'
    
    moves = p1.get_available_moves(board, ('e', 2))
    print(moves)
    moves = p2.get_available_moves(board, ('h', 7))
    print(moves)
    moves = p3.get_available_moves(board, ('e', 5))
    print(moves)
    '''
    
    # knight trials
    '''
    p4 = cp.Knight('white')
    print(board)
    print(board['d'].loc[6].get_colour())
    print(board['d'].loc[2].get_colour())
    moves = p4.get_available_moves(board, ('e', 4))
    print(moves)
    moves = p4.get_available_moves(board, ('g', 4))
    print(moves)
    moves = p4.get_available_moves(board, ('h', 7))
    print(moves)
    '''
    
    '''
    p5 = cp.King('white')
    print(p5.get_available_moves(board, ('e', 4)))
    print(p5.get_available_moves(board, ('f', 4)))
    '''
    
    '''
    p6 = cp.Bishop('white')
    print(p6.get_available_moves(board, ('e', 4)))
    
    p7 = cp.Rook('white')
    print(p7.get_available_moves(board, ('a', 1)))
    print(p7.get_available_moves(board, ('a', 2)))
    print(p7.get_available_moves(board, ('e', 4)))
    '''
    
    p8 = cp.Queen('white')
    print(p8.get_available_moves(board, ('a', 1)))
    print(p8.get_available_moves(board, ('a', 2)))
    print(p8.get_available_moves(board, ('e', 4)))
    print(p8.get_available_moves(board, ('b', 8)))
    
if __name__ == '__main__' :
    
    start_game()
