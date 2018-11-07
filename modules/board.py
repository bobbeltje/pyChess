
import pandas as pd
import random
#from . import utils
from . import pieces as cp
from . import glob_vars


def new_board() :

    board = pd.DataFrame([[0]*8]*8)
    board.columns = glob_vars.FILES
    board.index = glob_vars.RANKS

    white = dict()
    black = dict()

    # add pawns
    for i in range(8) :
        board.at[7, glob_vars.FILES[i]] = cp.Pawn(colour='black', name='pawn{0}'.format(i))
        board.at[2, glob_vars.FILES[i]] = cp.Pawn(colour='white', name='pawn'+str(i))
        white['pawn'+str(i)] = glob_vars.FILES[i] + str(2)
        black['pawn'+str(i)] = glob_vars.FILES[i] + str(7)

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
    
    Returns a dictionary
    {'e2e4':0, ...}
    '''
    
    moves = {}
    # per piece find the available moves and put in movelist
    for piece, pos in dic.items() :

        movelist = board.at[int(pos[1]), pos[0]].get_available_moves(
                board, (pos[0], int(pos[1]))
                )
        
        # if moves are available, find the value of those moves and then append
        if movelist :
#           
            for file,rank in movelist :
                
                value = 0
                
                if board.at[rank, file] :
                    value = board.at[rank, file].value
                    
                moves[pos+file+str(rank)] = value

    return moves

def search_move(board, dic, dic_opponent, depth, multiplier) :
    '''
    Calculate the next set of best moves
    '''

    glob_vars.moves_considered += 1

    available_moves = get_all_moves(board, dic)
    # result: {'e2e4':0, ...}
    
    max_gain = max(available_moves.values()) - 0.1
    
    if max_gain > 999 :
        for key,val in available_moves.items() :
            if val > 999 :
                ret_dic = {key : val*multiplier}
                break
        
        return ret_dic
    
    if depth == 0 :
    
        ret_dic = {}
        for key,val in available_moves.items() :
            if val > max_gain :
                ret_dic[key] = val*multiplier
        
        ret_move = random.choice(list(ret_dic.keys()))
        return {ret_move : ret_dic[ret_move]}
     
    deep_moves = []
    return_moves = {}
    for move in available_moves.keys() :
        new_board = board.copy()
        new_dic = dic.copy()
        new_opp = dic_opponent.copy()
        
        old_pos = (int(move[1]), move[0])
        new_pos = (int(move[3]), move[2])
        
        # in case piece is taken
        if new_board.at[new_pos] :
            del new_opp[new_board.at[new_pos].name]
            
        # move the piece
        new_board.loc[new_pos] = new_board.at[old_pos]
        new_board.loc[old_pos] = 0
        # update the dictionary
        new_dic[new_board.at[new_pos].name] = new_pos[1] + str(new_pos[0])
        
        # in case of promotion
        if (new_board.at[new_pos].name[:4] == 'pawn' 
          and new_pos[0] in (1,8) 
          and new_board.at[new_pos].piece_type == 'pawn') :
          
            new_board.loc[new_pos] = cp.Queen(new_board.at[new_pos].colour, 
                                             name=new_board.at[new_pos].name)
            
        # call recursively
        deep_moves = search_move(new_board, new_opp, new_dic, depth-1, multiplier*-1)
        
        # return chain of moves with value
        for new_move,val in deep_moves.items() :
            return_moves[move + new_move] = available_moves[move]*multiplier + val
            
    max_gain = max([val*multiplier for key,val in return_moves.items()]) - 0.1
    ret_dic = {}
    for key,val in return_moves.items() :
        if val*multiplier > max_gain :
            ret_dic[key] = val
    ret_move = random.choice(list(ret_dic.keys()))
    
    return {ret_move : ret_dic[ret_move]}
            
#board, white, black = tmp_board()
#x = search_move(board, white, black, 0, 1)

#for piece,pos in black.items():
#    print(piece)
#    print(pos)
#    print(
#    board.at[int(pos[1]), pos[0]].get_available_moves(board, (pos[0], int(pos[1])))
#            )
    
def make_move(board, dic, dic_opponent, col, player, depth) :
    
    if player == 'computer' :

        best_move = search_move(board, dic, dic_opponent, depth=depth, multiplier=1)
        best_move = list(best_move.keys())[0]
        old_pos = (int(best_move[1]), best_move[0])
        new_pos = (int(best_move[3]), best_move[2])
    
    if player == 'human' :
        
        best_move = make_human_move()
        old_pos = (int(best_move[1]), best_move[0])
        new_pos = (int(best_move[3]), best_move[2])

#    print(piece)
#    print(move)
    # NOTE 
    # piece in format a1, g2 etc
    # move in format ('h', 4)
    print('{0} moves {1} on {2}{3} to {4}{5}'.format(
            col, 
            board.at[old_pos].name, 
            old_pos[1],
            old_pos[0], 
            new_pos[1], 
            new_pos[0]))
    
    # in case piece is taken
    if board.at[new_pos] :
        if board.at[new_pos].name == 'king' :
            print('\n\n\n')
        print('taking {0}'.format(board.at[new_pos].name))
        del dic_opponent[board.at[new_pos].name]
        
    # move piece
    board.loc[new_pos] = board.at[old_pos]
    board.loc[new_pos].moved = True
    # set old location to 0
    board.loc[old_pos] = 0
    # update dictionary
    dic[board.at[new_pos].name] = new_pos[1]+str(new_pos[0])
    
    # promotion
    if (board.at[new_pos].name[:4] == 'pawn' 
        and new_pos[0] in (1,8) 
        and board.at[new_pos].piece_type == 'pawn'
        ):
        print('promotion!')
        print(dic)
        print('not' + col)
        print(dic_opponent)
        board.loc[new_pos] = cp.Queen(col, name=board.at[new_pos].name)
        
    return dic, dic_opponent


def print_debug_board(board, dic, dic_opponent, **kwargs) :
    
    for rank in range(1, 9) :
        print(rank)
        for file in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] :
            if type(board.at[rank, file]).__name__ not in ('int', 'FakePiece') :
                print(board.at[rank, file])
    print()
    print()
            
    print(dic)
    print(dic_opponent)

    print()
    print()
    
    for key,val in kwargs.items() :
        print(key)
        print(val)
        print()

    'a' + 5


def make_human_move() :
    
    print('Make your move!')
    return input()


def is_check_mate(board, dic, dic_opponent) :
    
    best_move = search_move(board, dic, dic_opponent, depth=1, multiplier=1)
    max_gain = abs(max(best_move.values()))
    
    if max_gain > 999 :
        
        return True
    
    return False

# UNUSED 
    
def get_ordered_move_values(moves) :
    '''
    Expects a list of all possible moves
    An element is a tuple: (position, available moves, values)
    
    Returns an ordered (decreasing) list of unique values
    '''
    values = set()
    
    for move in moves :
        values.update(list(move[2]))

    return sorted(list(values), reverse=True)
    
