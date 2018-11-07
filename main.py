
import modules.board as boards
import modules.glob_vars as glob_vars
import modules.utils as utils

import random
import time

#import modules.utils as utils
#import modules.pieces as cp
#from modules.board import *
#from modules.testcode import tmp_board

random.seed(5)

def start_game() :
    
    pause_every_ten_moves = True
    game_over = False
    div = 32.
    start_time = time.time()
    
    players = ['computer', 'computer']
    board, white, black = boards.new_board()
    
    pieceList = [white, black]
    colourList = ['white', 'black']
    
    move = 1
    glob_vars.moves_considered = 0
    while True :
        
        print()
        print()
        print('Move {0}'.format(move))
        for i in (0, 1) :
            
            print('moves considered: {}'.format(glob_vars.moves_considered))
            cur_depth = utils.get_depth(div, *pieceList)
            print('white/black piece: {}+{}, depth:{}'.format(
                    len(pieceList[0]),
                    len(pieceList[1]),
                    cur_depth))
            
            pieceList[i], pieceList[1-i] = boards.make_move(
                    board, 
                    pieceList[i], 
                    pieceList[1-i], 
                    colourList[i],
                    players[i],
                    depth=cur_depth)
            
#            if boards.is_check_mate(board, pieceList[1-i], pieceList[i]) :
            if 'king' not in pieceList[1-i] :
                print('{} has won the game!'.format(colourList[i]))
                game_over = True
                break
                            
        if game_over :
            
            break
        
        move += 1
        
        if pause_every_ten_moves and move % 10 == 0 :
            print()
            print(white)
            print(black)
#            input('Press [enter]')
#        if move == 10 :
#            break
#        input('[enter]')
            
    print(start_time - time.time())
    
if __name__ == '__main__' :

    start_game()

