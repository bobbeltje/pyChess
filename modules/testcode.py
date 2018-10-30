import pandas as pd

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
