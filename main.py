
import pandas as pd
import modules.pieces as cp
import modules.utils as utils
# from modules.utils import *

# Note that the indeces of FILES & RANKS go from 0 to 7
FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]

# Note consider using two dictionaries to hold the positions        

def start_game() :
    
    global FILES, RANKS
    
    board, white, black = utils.new_board()
    
    '''
    print(board)
    print(white)
    print(black)
    #'''
    
    '''
    print(board.index)
    print(type(board.index[1]))
    print(type(board.columns[1]))
    #'''
    
    
    moves = []
    for piece, pos in white.items() :
        # print('piece:{0} ; pos0: {1} ; pos1: {2}'.format(piece, pos[0], pos[1]))
        movelist = board.loc[int(pos[1]), pos[0]].get_available_moves(board, (pos[0], int(pos[1])))
        moves.append((pos, movelist))
        
    print(moves)
    
if __name__ == '__main__' :
    
    start_game()
