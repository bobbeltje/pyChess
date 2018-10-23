
#import pandas as pd

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [i for i in range(1, 9)]


def get_file(cur, direction, number) :
    
    global FILES
    
    file_index = FILES.index(cur)
    
    if direction == 'left' :
        if file_index - number < 0 :
            return False
        return FILES[file_index - number]
        
    if direction == 'right' :
        if file_index + number > 7 :
            return False
        return FILES[file_index + number]

