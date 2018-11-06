
import modules.board as boards
import modules.glob_vars as glob_vars
import random

#import modules.utils as utils
#import modules.pieces as cp
#from modules.board import *
#from modules.testcode import tmp_board

random.seed(5)
# Note consider using two dictionaries to hold the positions

# strat3 other.value - own.value        

def start_game() :
        
    players = ['computer', 'computer']
    board, white, black = boards.new_board()
    
    #for i in range(1, 9) :
    #    print(board.loc[i])
    '''
    print(board)
    print(white)
    print(black)
    #'''
    pieceList = [white, black]
    colourList = ['white', 'black']
    
    move = 1
    glob_vars.moves_considered = 0
    while True :
        
        print('Move {0}'.format(move))
        for i in (0, 1) :
            
#            pieceList[i], pieceList[1-i] = boards.make_move(board, pieceList[i], pieceList[1-i], colourList[i])
            if players[i] == 'computer' :
                pieceList[i], pieceList[1-i] = boards.make_best_move(board, pieceList[i], pieceList[1-i], colourList[i])
            else :
                pieceList[i], pieceList[1-i] = boards.make_human_move(board, pieceList[i], pieceList[1-i], colourList[i])
                            
        move += 1
#        input('[enter]')
    
    # boards.make_move(board, white)
    # print(board)
    # print(pieceList[0])
    # print(pieceList[1])
    
#    for file_ in board.columns :
#        print(board[file_])
    
if __name__ == '__main__' :

    start_game()

