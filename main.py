
import modules.board as boards
import random

# Note that the indeces of FILES & RANKS go from 0 to 7
FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]
random.seed(5)
# Note consider using two dictionaries to hold the positions        

def start_game() :
    
    global FILES, RANKS
    
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
    while True :
        
        print('Move {0}'.format(move))
        for i in (0, 1) :
            
            pieceList[i], pieceList[1-i] = boards.make_move(board, pieceList[i], pieceList[1-i], colourList[i])
            
        move += 1
        input('[enter]')
    
    # boards.make_move(board, white)
    # print(board)
    # print(pieceList[0])
    # print(pieceList[1])
    
#    for file_ in board.columns :
#        print(board[file_])
    
if __name__ == '__main__' :
    
    start_game()
