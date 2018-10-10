
from modules.utils import *
# from utils import *
import math

class Pawn() :
    
    def __init__(self, colour) :
        
        self.piece_type = 'pawn'
        self.colour = colour
        self.enpassant = False

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        right_file = get_file(pos[0], 'right', 1)
        left_file = get_file(pos[0], 'left', 1)
        
        if self.colour == 'white' :
            
            # check if a piece can be taken left
            if left_file :
                if board[left_file][pos[1]+1] :
                    if board[left_file][pos[1]+1].get_colour() != 'white' :
                        moves.append((left_file, pos[1]+1))
            # check if a piece can be taken right
            if right_file :
                if board[right_file][pos[1]+1] :
                    if board[right_file][pos[1]+1].get_colour() != 'white' :
                        moves.append((right_file, pos[1]+1))
            # check if it can take one step
            if not board[pos[0]][pos[1]+1] :
                moves.append((pos[0], pos[1]+1))
            # check if it can take two steps
            if not board[pos[0]][pos[1]+1] and not board[pos[0]][pos[1]+2] and pos[1]==2:
                moves.append((pos[0], pos[1]+2))
            if self.enpassant :
                moves.append((self.enpassant, 6))
                self.enpassant = False
                
            return moves
        
        if self.colour == 'black' :
            
            # check if a piece can be taken left
            if left_file :
                if board[left_file][pos[1]-1] :
                    if board[left_file][pos[1]-1].get_colour() != 'black' :
                        moves.append((left_file, pos[1]-1))
            # check if a piece can be taken right
            if right_file :
                if board[right_file][pos[1]-1] :
                    if board[right_file][pos[1]-1].get_colour() != 'black' :
                        moves.append((right_file, pos[1]-1))
            # check if it can take one step
            if not board[pos[0]][pos[1]-1] :
                moves.append((pos[0], pos[1]-1))
            # check if it can take two steps
            if not board[pos[0]][pos[1]-1] and not board[pos[0]][pos[1]-2] and pos[1]==7:
                moves.append((pos[0], pos[1]-2))
            if self.enpassant :
                moves.append((self.enpassant, 3))
                self.enpassant = False
                
            return moves
            
class WhitePawn(Pawn) :
    pass
    
class BlackPawn(Pawn) :
    pass
    

class Knight() :
    
    def __init__(self, colour) :
        
        self.piece_type = 'knight'
        self.colour = colour

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # check one file to the right
        for direction in ('left', 'right') :
            for side_step in (1, 2) :
                rank_change = 3 - side_step
                new_file = get_file(pos[0], direction, side_step)
                if new_file :
                    # moving up
                    if pos[1] + rank_change <= 8 :
                        if not board[new_file][pos[1]+rank_change] :
                            moves.append((new_file, pos[1]+rank_change))
                        else :
                            if board[new_file][pos[1]+rank_change].get_colour() != self.colour :
                                moves.append((new_file, pos[1]+rank_change))
                    # moving down
                    if pos[1] - rank_change >= 1 :
                        if not board[new_file][pos[1]-rank_change] :
                            moves.append((new_file, pos[1]-rank_change))
                        else :
                            if board[new_file][pos[1]-rank_change].get_colour() != self.colour :
                                moves.append((new_file, pos[1]-rank_change))
                            
        return moves
                
class Bishop() :
    
    def __init__(self, colour) :
        
        self.piece_type = 'bishop'
        self.colour = colour

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # check one file to the right
        for direction in ('left', 'right') :
            for step in (1, -1) :
                piece_encountered = False
                while True :
                    new_file = get_file(pos[0], direction, abs(step))
                    if new_file :
                        if pos[1] + step <= 8  and pos[1] + step >= 1:
                            if not board[new_file][pos[1]+step] :
                                moves.append((new_file, pos[1]+step))
                            else :
                                piece_encountered = True
                                if board[new_file][pos[1]+step].get_colour() != self.colour :
                                    moves.append((new_file, pos[1]+step))
                    if not new_file or piece_encountered :
                        break
                    step += int(math.copysign(1, step))
        return moves

class Rook() :
    
    def __init__(self, colour) :
        
        self.piece_type = 'rook'
        self.colour = colour
        
    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        pass

                    
class King() :
    
    def __init__(self, colour) :
        
        self.piece_type = 'king'
        self.colour = colour

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # bishop-like movement
        for direction in ('left', 'right') :
            for step in (1, -1) :
                new_file = get_file(pos[0], direction, abs(step))
                if new_file :
                    if pos[1] + step <= 8  and pos[1] + step >= 1:
                        if not board[new_file][pos[1]+step] :
                            moves.append((new_file, pos[1]+step))
                        else :
                            piece_encountered = True
                            if board[new_file][pos[1]+step].get_colour() != self.colour :
                                moves.append((new_file, pos[1]+step))
        
        # rook-like movement
        
        # check for castling
        
        return moves
                     
            
                    
            
                    
