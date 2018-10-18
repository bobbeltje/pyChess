
import pandas as pd
import random
from . import utils
from . import pieces as cp

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]


def new_board() :

    global FILES, RANKS
    
    board = pd.DataFrame([[0]*8]*8)
    board.columns = FILES
    board.index = RANKS

    white = dict()
    black = dict()

    # add pawns
    for i in range(8) :
        board[FILES[i]].loc[7] = cp.Pawn(colour='black', name='pawn{0}'.format(i))
        board[FILES[i]].loc[2] = cp.Pawn(colour='white', name='pawn'+str(i))
        white['pawn'+str(i)] = FILES[i] + str(2)
        black['pawn'+str(i)] = FILES[i] + str(7)

    board['a'].loc[1] = cp.Rook('white', name='rook0')
    board['b'].loc[1] = cp.Knight('white', name='knight0')
    board['c'].loc[1] = cp.Bishop('white', name='bishop0')
    board['d'].loc[1] = cp.Queen('white')
    board['e'].loc[1] = cp.King('white')
    board['f'].loc[1] = cp.Bishop('white', name='bishop1')
    board['g'].loc[1] = cp.Knight('white', name='knight1')
    board['h'].loc[1] = cp.Rook('white', name='rook1')
    board['a'].loc[8] = cp.Rook('black', name='rook0')
    board['b'].loc[8] = cp.Knight('black', name='knight0')
    board['c'].loc[8] = cp.Bishop('black', name='bishop0')
    board['d'].loc[8] = cp.Queen('black')
    board['e'].loc[8] = cp.King('black')
    board['f'].loc[8] = cp.Bishop('black', name='bishop1')
    board['g'].loc[8] = cp.Knight('black', name='knight1')
    board['h'].loc[8] = cp.Rook('black', name='rook1')


    white.update({'rook0':'a1', 'knight0':'b1', 'bishop0':'c1', 'queen':'d1',
             'king':'e1', 'bishop1':'f1', 'knight1':'g1', 'rook1':'h1'})
    black.update({'rook0':'a8', 'knight0':'b8', 'bishop0':'c8', 'queen':'d8',
             'king':'e8', 'bishop1':'f8', 'knight1':'g8', 'rook1':'h8'})
    
    return board, white, black

def make_move(board, dic, dic_opponent, col) :

    moves = []
    for piece, pos in dic.items() :
        try :
            movelist = board.loc[int(pos[1]), pos[0]].get_available_moves(board, (pos[0], int(pos[1])))
        except :
            print('piece:{0} ; pos0: {1} ; pos1: {2}'.format(piece, pos[0], pos[1]))
        
        if movelist :
            moves.append((pos, movelist))
        
    piece = random.choice(moves)
    move = random.choice(piece[1])
    piece = piece[0]

    print('{3} moves {0} to {1}{2}'.format(piece, move[0], move[1], col))
    
    # in case piece is taken
    if board.loc[move[1], move[0]] :
        print('taking {0}'.format(board.loc[move[1], move[0]].name))
        del dic_opponent[board.loc[move[1], move[0]].name]
        
    # move piece
    board.loc[move[1], move[0]] = board.loc[int(piece[1]), piece[0]]
    # set old location to 0
    board.loc[int(piece[1]), piece[0]] = 0
    # update dictionary
    dic[board.loc[int(move[1]), move[0]].name] = move[0]+str(move[1])
    
    return dic, dic_opponent
    
    
