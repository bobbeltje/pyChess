FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]
from . import pieces as cp

import pandas as pd

def cur_board() :

    global FILES, RANKS
    
    board = pd.DataFrame([[0]*8]*8)
    board.columns = FILES
    board.index = RANKS
    
    board.at[1, 'd'] = cp.Rook('white', 'rook0')
    board.at[1, 'f'] = cp.Rook('white', 'rook1')
    board.at[1, 'g'] = cp.King('white', 'king')
    board.at[2, 'a'] = cp.Pawn('white', 'pawn0')
    board.at[2, 'b'] = cp.Pawn('white', 'pawn1')
    board.at[3, 'd'] = cp.Bishop('white', 'bishop0')
    board.at[3, 'g'] = cp.Pawn('white', 'pawn2')
    board.at[4, 'c'] = cp.Pawn('white', 'pawn3')
    board.at[5, 'a'] = cp.Bishop('white', 'bishop1')
    board.at[5, 'd'] = cp.Knight('white', 'knight0')
    board.at[5, 'h'] = cp.Pawn('white', 'pawn4')
    
    board.at[8, 'b'] = cp.Knight('black', 'knight0')
    board.at[8, 'f'] = cp.Bishop('black', 'bishop0')
    board.at[8, 'g'] = cp.Knight('black', 'knight1')
    board.at[8, 'h'] = cp.Rook('black', 'rook0')
    board.at[7, 'c'] = cp.Pawn('black', 'pawn0')
    board.at[7, 'd'] = cp.Pawn('black', 'pawn1')
    board.at[7, 'e'] = cp.Pawn('black', 'pawn2')
    board.at[7, 'f'] = cp.King('black', 'king')
    board.at[7, 'g'] = cp.Pawn('black', 'pawn3')
    board.at[6, 'h'] = cp.Pawn('black', 'pawn4')
    board.at[5, 'e'] = cp.Pawn('black', 'pawn5')
    board.at[4, 'a'] = cp.Queen('black', 'queen')

    white = {'rook0':'d1', 'rook1':'f1', 'king':'g1', 'pawn0':'a2',
             'pawn1':'b2', 'bishop0':'d3', 'pawn2':'g3', 'pawn3':'c4',
             'bishop1':'a5', 'knight0':'d5', 'pawn4':'h5'}
    black = {'knight0':'b8', 'bishop0':'f8', 'knight1':'g8', 'rook0':'h8',
             'pawn0':'c7', 'pawn1':'d7', 'pawn2':'e7', 'king':'f7',
             'pawn3':'g7', 'pawn4':'h6', 'pawn5':'e5', 'queen':'a4'}
    
    return board, white, black

def tmp_board() :

    global FILES, RANKS
    
    board = pd.DataFrame([[cp.FakePiece(colour='black')]*8]*8)
    board.columns = FILES
    board.index = RANKS

    white = dict()
    black = dict()
    
    board.at[4, 'a'] = cp.Rook('white', name='rook0')
    board.at[4, 'e'] = cp.Knight('white', name='knight0')
    board.at[5, 'g'] = cp.Bishop('white', name='bishop0')
    board.at[6, 'b'] = cp.Knight('black', name='knight0')
    board.at[7, 'e'] = cp.King('black', name='king0')
    board.at[6, 'f'] = cp.Knight('black', name='knight1')
    board.at[4, 'h'] = cp.Rook('black', name='rook0')
    board.at[5, 'd'] = 0
    
    white.update({'bishop0' : 'g5', 'knight0' : 'e4', 'rook0':'a4'})
    black.update({'knight0':'b6', 'king0':'e7', 'knight1':'f6', 'rook0':'h4'})
    
    return board, white, black


'''
def tmp_board() :

    global FILES, RANKS
    
    board = pd.DataFrame([[0]*8]*8)
    board.columns = FILES
    board.index = RANKS

    white = dict()
    black = dict()
    
    board.at[5, 'a'] = cp.Rook('white', name='rook0')
    board.at[3, 'b'] = cp.Bishop('white', name='bishop0')
    board.at[3, 'c'] = cp.Knight('white', name='knight0')
    board.at[4, 'e'] = cp.Pawn('white', name='pawn0')
    board.at[7, 'c'] = cp.Knight('black', name='knight0')
    board.at[7, 'd'] = cp.Queen('black', name='queen0')
    board.at[5, 'd'] = cp.Pawn('black', name='pawn0')
    board.at[6, 'e'] = cp.Pawn('black', name='pawn1')
    board.at[5, 'h'] = cp.Rook('black', name='rook0')

    white.update({'rook0' : 'a5', 'bishop0' : 'b3', 'knight0' : 'c3',
                  'pawn0' : 'e4'})
    black.update({'knight0':'c7', 'queen0':'d7', 'pawn0' : 'd5', 
                  'pawn1' : 'e6', 'rook0' : 'h5'})
    
    return board, white, black
'''
'''            
def f2(n) :
    if n == 0 :
        return ['a', 'b']
    l2 = []
    moves = ['a', 'b']
    for move in moves :
        x = f2(n-1)
        for i in x :
            l2.append(move+i)
    return l2
f2(0)
f2(1)
f2(2)
f2(3)
'''


# pawn trials
'''
print('pawn trials')
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
print('knight trials')
p4 = cp.Knight('white')
moves = p4.get_available_moves(board, ('e', 4))
print(moves)
moves = p4.get_available_moves(board, ('g', 4))
print(moves)
moves = p4.get_available_moves(board, ('h', 7))
print(moves)
'''

'''
print('king trials')
p5 = cp.King('white')
print(p5.get_available_moves(board, ('e', 4)))
print(p5.get_available_moves(board, ('f', 4)))
'''

'''
print('bishop trials')
p6 = cp.Bishop('white')
print(p6.get_available_moves(board, ('e', 4)))

p7 = cp.Rook('white')
print(p7.get_available_moves(board, ('a', 1)))
print(p7.get_available_moves(board, ('a', 2)))
print(p7.get_available_moves(board, ('e', 4)))
'''

'''
print('queen trials')
p8 = cp.Queen('white')
print(p8.get_available_moves(board, ('a', 1)))
print(p8.get_available_moves(board, ('a', 2)))
print(p8.get_available_moves(board, ('e', 4)))
print(p8.get_available_moves(board, ('b', 8)))
'''
