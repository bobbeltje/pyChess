
from utils import *

class Pawn() :
    
    def __init__(self, colour) :
        
        self.piece_type = 'pawn'
        self.colour = colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        if self.colour == 'white' :
            
            # check if a piece can be taken left
            if board[get_file(pos[0], 'left')][pos[1]+1] :
                if board[get_file(pos[0], 'left')][pos[1]+1].get_colour != 'white' :
                    moves.append((get_file(pos[0], 'left'), pos[1]+1))
            # check if a piece can be taken right
            if board[get_file(pos[0], 'right')][pos[1]+1] :
                if board[get_file(pos[0], 'right')][pos[1]+1].get_colour != 'white' :
                    moves.append((get_file(pos[0], 'right'), pos[1]+1))
            # check if it can take one step
            if not board[pos[0]][pos[1]+1] :
                moves.append((pos[0], pos[1]+1))
            # check if it can take two steps
            if not board[pos[0]][pos[1]+1] and not board[pos[0]][pos[1]+2] and pos[1]==2:
                moves.append((pos[0], pos[1]+2))
                
            return moves
        
        if self.colour == 'black' :
            
            # check if a piece can be taken left
            if board[get_file(pos[0], 'left')][pos[1]-1] :
                if board[get_file(pos[0], 'left')][pos[1]-1].get_colour != 'black' :
                    moves.append((get_file(pos[0], 'left'), pos[1]-1))
            # check if a piece can be taken right
            if board[get_file(pos[0], 'right')][pos[1]-1] :
                if board[get_file(pos[0], 'right')][pos[1]-1].get_colour != 'black' :
                    moves.append((get_file(pos[0], 'right'), pos[1]-1))
            # check if it can take one step
            if not board[pos[0]][pos[1]-1] :
                moves.append((pos[0], pos[1]-1))
            # check if it can take two steps
            if not board[pos[0]][pos[1]-1] and not board[pos[0]][pos[1]-2] and pos[1]==7:
                moves.append((pos[0], pos[1]-2))
                
            return moves
                
                    
            
                    
