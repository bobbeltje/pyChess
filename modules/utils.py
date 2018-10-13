
import pandas as pd
import pieces as cp

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
        board[FILES[i]].loc[7] = cp.Pawn('black')
        board[FILES[i]].loc[2] = cp.Pawn('white')

    board['a'].loc[1] = cp.Rook('white')
    board['b'].loc[1] = cp.Knight('white')
    board['c'].loc[1] = cp.Bishop('white')
    board['d'].loc[1] = cp.Queen('white')
    board['e'].loc[1] = cp.King('white')
    board['f'].loc[1] = cp.Bishop('white')
    board['g'].loc[1] = cp.Knight('white')
    board['h'].loc[1] = cp.Rook('white')
    board['a'].loc[8] = cp.Rook('black')
    board['b'].loc[8] = cp.Knight('black')
    board['c'].loc[8] = cp.Bishop('black')
    board['d'].loc[8] = cp.Queen('black')
    board['e'].loc[8] = cp.King('black')
    board['f'].loc[8] = cp.Bishop('black')
    board['g'].loc[8] = cp.Knight('black')
    board['h'].loc[8] = cp.Rook('black')

    return board
