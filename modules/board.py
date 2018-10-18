
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
        board.at[7, FILES[i]] = cp.Pawn(colour='black', name='pawn{0}'.format(i))
        board.at[2, FILES[i]] = cp.Pawn(colour='white', name='pawn'+str(i))
        white['pawn'+str(i)] = FILES[i] + str(2)
        black['pawn'+str(i)] = FILES[i] + str(7)

    board.at[1, 'a'] = cp.Rook('white', name='rook0')
    board.at[1, 'b'] = cp.Knight('white', name='knight0')
    board.at[1, 'c'] = cp.Bishop('white', name='bishop0')
    board.at[1, 'd'] = cp.Queen('white')
    board.at[1, 'e'] = cp.King('white')
    board.at[1, 'f'] = cp.Bishop('white', name='bishop1')
    board.at[1, 'g'] = cp.Knight('white', name='knight1')
    board.at[1, 'h'] = cp.Rook('white', name='rook1')
    board.at[8, 'a'] = cp.Rook('black', name='rook0')
    board.at[8, 'b'] = cp.Knight('black', name='knight0')
    board.at[8, 'c'] = cp.Bishop('black', name='bishop0')
    board.at[8, 'd'] = cp.Queen('black')
    board.at[8, 'e'] = cp.King('black')
    board.at[8, 'f'] = cp.Bishop('black', name='bishop1')
    board.at[8, 'g'] = cp.Knight('black', name='knight1')
    board.at[8, 'h'] = cp.Rook('black', name='rook1')


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
            'a' + 4
        
        if movelist :
            moves.append((pos, movelist))
        
    piece = random.choice(moves)
    move = random.choice(piece[1])
    piece = piece[0]
    
    # NOTE 
    # piece in format a1, g2 etc
    # move in format ('h', 4)
    print('{0} moves {1} on {2} to {3}{4}'.format(col, board.loc[int(piece[1]), piece[0]].name, piece, move[0], move[1]))
    
    # in case piece is taken
    if board.loc[move[1], move[0]] :
        if board.loc[move[1], move[0]].name == 'king' :
            print('\n\n\n')
        print('taking {0}'.format(board.loc[move[1], move[0]].name))
        del dic_opponent[board.loc[move[1], move[0]].name]
        
    # move piece
    board.loc[move[1], move[0]] = board.loc[int(piece[1]), piece[0]]
    # set old location to 0
    board.loc[int(piece[1]), piece[0]] = 0
    # update dictionary
    dic[board.loc[int(move[1]), move[0]].name] = move[0]+str(move[1])
    
    # promotion
    if board.loc[move[1], move[0]].name[:4] == 'pawn' and move[1] in (1,8) and board.loc[move[1], move[0]].piece_type == 'pawn' :
        print('promotion!')
        print(dic)
        print('not' + col)
        print(dic_opponent)
        board.at[int(move[1]), move[0]] = cp.Queen(col, name=board.loc[move[1], move[0]].name)
        
    return dic, dic_opponent
    
    
