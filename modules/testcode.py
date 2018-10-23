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
