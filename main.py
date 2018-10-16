
import modules.board as boards

# Note that the indeces of FILES & RANKS go from 0 to 7
FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]

# Note consider using two dictionaries to hold the positions        

def start_game() :
    
    global FILES, RANKS
    
    board, white, black = boards.new_board()
    
    '''
    print(board)
    print(white)
    print(black)
    #'''
    pieceList = [white, black]
    colourList = ['white', 'black']
    
    while True :
        
        for i in (0, 1) :
        
            pieceList[i] = boards.make_move(board, pieceList[i], colourList[i])
    
    # boards.make_move(board, white)
    # print(board)
    # print(pieceList[0])
    # print(pieceList[1])
    
#    for file_ in board.columns :
#        print(board[file_])
    
if __name__ == '__main__' :
    
    start_game()
