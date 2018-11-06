
import modules.board as boards
import modules.glob_vars as glob_vars

import random
import time

#import modules.utils as utils
#import modules.pieces as cp
#from modules.board import *
#from modules.testcode import tmp_board

random.seed(5)

def start_game() :
        
    start_time = time.time()
    
    players = ['computer', 'computer']
    board, white, black = boards.new_board()
    
    pieceList = [white, black]
    colourList = ['white', 'black']
    
    move = 1
    glob_vars.moves_considered = 0
    while True :
        
        print('Move {0}'.format(move))
        for i in (0, 1) :
            
            print('moves considered: {}'.format(glob_vars.moves_considered))

            pieceList[i], pieceList[1-i] = boards.make_move(
                    board, 
                    pieceList[i], 
                    pieceList[1-i], 
                    colourList[i],
                    players[i])
                            
        move += 1
#        if move == 10 :
#            break
#        input('[enter]')
            
    print(start_time - time.time())
    
if __name__ == '__main__' :

    start_game()

