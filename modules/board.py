
import pandas as pd
import random
#from . import utils
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

def get_all_moves(board, dic) :
    '''
    Find all possible moves for the pieces in dic.
    
    Returns a list of tuples
    tuple[0] is the position of a piece
    tuple[1] is the available moves for that piece
    tuple[2] is the value of pieces it can capture
    '''
    
    moves = []
    # per piece find the available moves and put in movelist
    for piece, pos in dic.items() :
        try :
            movelist = board.loc[int(pos[1]), pos[0]].get_available_moves(
                            board, (pos[0], int(pos[1]))
                            )
        except :
            for i in range(3, 8) :
                print(board.loc[i])
            print('piece:{0} ; pos0: {1} ; pos1: {2}'.format(piece, 
                                                             pos[0], 
                                                             pos[1]))
            print(dic)
            'a' + 5
        
        # if moves are available, find the value of those moves and then append
        if movelist :
#            values = np.random.normal(len(movelist), scale=0.05)
            values = [0] * len(movelist)
            for idx in range(len(movelist)) :
                rank, file = movelist[idx]
                if board.loc[file, rank] :
                    values[idx] = board.loc[file, rank].value
                    
            moves.append((pos, movelist, values))
            
    return moves

def search_move(board, dic, dic_opponent, depth, multiplier) :
    '''
    Calculate the next set of best moves
    '''
    available_moves = get_all_moves(board, dic)
    good_moves = {}
    
    # extract the highest valued moves
    # result {'e2e4':0}
    for piece_idx in range(len(available_moves)) :
        for move_idx in range(len(available_moves[piece_idx][1])) :
            if available_moves[piece_idx][2][move_idx] > 0.01 :
                good_moves[
                        '{0}{1}{2}'.format(
                        available_moves[piece_idx][0],
                        available_moves[piece_idx][1][move_idx][0],
                        available_moves[piece_idx][1][move_idx][1])
                        ] = available_moves[piece_idx][2][move_idx] * multiplier
       
    if depth == 0 :
        return good_moves
         
    deep_moves = []
    return_moves = {}
    for move in good_moves.keys() :
        new_board = board.copy()
        new_dic = dic.copy()
        new_opp = dic_opponent.copy()
        
        old_pos = (int(move[1]), move[0])
        new_pos = (int(move[3]), move[2])
        
        # in case piece is taken
        if new_board.at[new_pos] :
            del new_opp[new_board.at[new_pos].name]

        # move the piece
        new_board.at[new_pos] = new_board.at[old_pos]
        new_board.at[old_pos] = 0
        # update the dictionary
        new_dic[new_board.loc[new_pos].name] = new_pos[1] + str(new_pos[0])
        
        # in case of promotion
        if (new_board.at[new_pos].name[:4] == 'pawn' 
          and new_pos[1] in (1,8) 
          and new_board.at[new_pos].piece_type == 'pawn') :
          
            new_board.at[new_pos] = cp.Queen(new_board.at[new_pos].colour, 
                                             name=new_board.at[new_pos].name)
            
        # call recursively
        deep_moves = search_move(new_board, new_opp, new_dic, depth-1, multiplier*-1)
        
        # return chain of moves with value
        for new_move,val in deep_moves.items() :
            return_moves[move + new_move] = good_moves[move] + val
            
    return return_moves
        
#board, white, black = tmp_board()
#x = search_move(board, black, white, 0, 1)

#for piece,pos in black.items():
#    print(piece)
#    print(pos)
#    print(
#    board.at[int(pos[1]), pos[0]].get_available_moves(board, (pos[0], int(pos[1])))
            )
    
def make_move(board, dic, dic_opponent, col) :
    
    moves = get_all_moves(board, dic)
#    strategy 01 : random choice
#    piece = random.choice(moves)
#    move = random.choice(piece[1])

#    strategy 02 : first best move
#    find the highest values each piece can score and the max of those
    highest_values = [max(k) for i,j,k in moves]
    max_value = max(highest_values) - 0.01
#    select one of the pieces that can gain max_value
    piece = random.choice([move for i,move in enumerate(moves) if max(moves[i][2]) >= max_value])
#    select one of its moves that gain max_value
    move = random.choice([idx for idx,val in enumerate(piece[2]) if val >= max_value])
    move = piece[1][move]
    
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
    
    
