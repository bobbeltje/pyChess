
import math
from . import utils


class Pawn() :
    
    def __init__(self, colour, name='pawn') :
        
        self.piece_type = 'pawn'
        self.colour = colour
        self.enpassant = False
        self.name = name

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        right_file = utils.get_file(pos[0], 'right', 1)
        left_file = utils.get_file(pos[0], 'left', 1)
        
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
            if pos[1]==2:
                if not board[pos[0]][pos[1]+1] and not board[pos[0]][pos[1]+2]: 
                    moves.append((pos[0], pos[1]+2))
            # enpassant
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
            if pos[1]==7: 
                if not board[pos[0]][pos[1]-1] and not board[pos[0]][pos[1]-2] :
                    moves.append((pos[0], pos[1]-2))
            # enpassant
            if self.enpassant :
                moves.append((self.enpassant, 3))
                self.enpassant = False
                
            return moves
            
class Knight() :
    
    def __init__(self, colour, name='knight') :
        
        self.piece_type = 'knight'
        self.colour = colour
        self.name = name

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # check one file to the right
        for direction in ('left', 'right') :
            for side_step in (1, 2) :
                rank_change = 3 - side_step
                new_file = utils.get_file(pos[0], direction, side_step)
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
    
    def __init__(self, colour, name='bishop') :
        
        self.piece_type = 'bishop'
        self.colour = colour
        self.name = name

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # check one file to the right
        for direction in ('left', 'right') :
            for step in (1, -1) :
                piece_encountered = False
                while True :
                    new_file = utils.get_file(pos[0], direction, abs(step))
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
    
    def __init__(self, colour, name='rook') :
        
        self.piece_type = 'rook'
        self.colour = colour
        self.moved = False
        self.name = name
        
    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # checking left and right
        for direction in ('left', 'right') :
            piece_encountered = False
            step = 1
            while True :
                new_file = utils.get_file(pos[0], direction, step)
                if new_file :
                    if not board[new_file][pos[1]] :
                        moves.append((new_file, pos[1]))
                    else :
                        piece_encountered = True
                        if board[new_file][pos[1]].get_colour() != self.colour :
                            moves.append((new_file, pos[1]))
                if not new_file or piece_encountered :
                    break
                step += 1

        # checking up and down
        for step in (-1, 1) :
            piece_encountered = False
            while (pos[1] + step > 0) and (pos[1] + step < 9) :
                if not board[pos[0]][pos[1]+step] :
                    moves.append((pos[0], pos[1]+step))
                else :
                    piece_encountered = True
                    if board[pos[0]][pos[1]+step].get_colour() != self.colour :
                        moves.append((pos[0], pos[1]+step))
                if piece_encountered :
                    break
                step += int(math.copysign(1, step))
                
        return moves

class King() :
    
    def __init__(self, colour, name='king') :
        
        self.piece_type = 'king'
        self.colour = colour
        self.moved = False
        self.name = name

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # bishop-like movement
        for direction in ('left', 'right') :
            for step in (1, -1) :
                new_file = utils.get_file(pos[0], direction, abs(step))
                if new_file :
                    if pos[1] + step <= 8  and pos[1] + step >= 1:
                        if not board[new_file][pos[1]+step] :
                            moves.append((new_file, pos[1]+step))
                        else :
                            piece_encountered = True
                            if board[new_file][pos[1]+step].get_colour() != self.colour :
                                moves.append((new_file, pos[1]+step))
        
        # rook-like movement
        # checking left and right
        for direction in ('left', 'right') :
            new_file = utils.get_file(pos[0], direction, 1)
            if new_file :
                if not board[new_file][pos[1]] :
                    moves.append((new_file, pos[1]))
                else :
                    if board[new_file][pos[1]].get_colour() != self.colour :
                        moves.append((new_file, pos[1]))

        # checking up and down
        for step in (-1, 1) :
            if pos[1] + step <= 8  and pos[1] + step >= 1:
                if not board[pos[0]][pos[1]+step] :
                    moves.append((pos[0], pos[1]+step))
                else :
                    if board[pos[0]][pos[1]+step].get_colour() != self.colour :
                        moves.append((pos[0], pos[1]+1))
        
        # check for castling
        
        return moves

class Queen() :
    
    def __init__(self, colour, name='queen') :
        
        self.piece_type = 'queen'
        self.colour = colour
        self.name = name

    def get_colour(self) :
        return self.colour
        
    def get_available_moves(self, board, pos) :
        
        moves = []
        
        # bishop-like movement
        # check one file to the right
        for direction in ('left', 'right') :
            for step in (1, -1) :
                piece_encountered = False
                while True :
                    new_file = utils.get_file(pos[0], direction, abs(step))
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
        
        # rook-like movement
        # checking left and right
        for direction in ('left', 'right') :
            piece_encountered = False
            step = 1
            while True :
                new_file = utils.get_file(pos[0], direction, step)
                if new_file :
                    if not board[new_file][pos[1]] :
                        moves.append((new_file, pos[1]))
                    else :
                        piece_encountered = True
                        if board[new_file][pos[1]].get_colour() != self.colour :
                            moves.append((new_file, pos[1]))
                if not new_file or piece_encountered :
                    break
                step += 1

        # checking up and down
        for step in (-1, 1) :
            piece_encountered = False
            while (pos[1] + step > 0) and (pos[1] + step < 9) :
                if not board[pos[0]][pos[1]+step] :
                    moves.append((pos[0], pos[1]+step))
                else :
                    piece_encountered = True
                    if board[pos[0]][pos[1]+step].get_colour() != self.colour :
                        moves.append((pos[0], pos[1]+step))
                if piece_encountered :
                    break
                step += int(math.copysign(1, step))
        
        return moves




