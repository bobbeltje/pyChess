
import pandas as pd
from . import pieces as cp

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]


def get_file(cur, direction, number) :
    
    global FILES
    
    file_index = FILES.index(cur)
    
    if direction == 'left' :
        if file_index - number < 0 :
            return False
        return FILES[file_index - number]
        
    if direction == 'right' :
        if file_index + number > 7 :
            return False
        return FILES[file_index + number]

def new_board() :

    global FILES, RANKS
    
    board = pd.DataFrame([[0]*8]*8)
    board.columns = FILES
    board.index = RANKS

    # add pawns
    for i in range(8) :
        board.loc[7, FILES[i]] = cp.Pawn('black')
        board.loc[2, FILES[i]] = cp.Pawn('white')

    board.loc[1, 'a'] = cp.Rook('white')
    board.loc[1, 'b'] = cp.Knight('white')
    board.loc[1, 'c'] = cp.Bishop('white')
    board.loc[1, 'd'] = cp.Queen('white')
    board.loc[1, 'e'] = cp.King('white')
    board.loc[1, 'f'] = cp.Bishop('white')
    board.loc[1, 'g'] = cp.Knight('white')
    board.loc[1, 'h'] = cp.Rook('white')
    board.loc[8, 'a'] = cp.Rook('black')
    board.loc[8, 'b'] = cp.Knight('black')
    board.loc[8, 'c'] = cp.Bishop('black')
    board.loc[8, 'd'] = cp.Queen('black')
    board.loc[8, 'e'] = cp.King('black')
    board.loc[8, 'f'] = cp.Bishop('black')
    board.loc[8, 'g'] = cp.Knight('black')
    board.loc[8, 'h'] = cp.Rook('black')

    return board
