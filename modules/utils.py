
import math
#import pandas as pd
from . import glob_vars

def get_file(cur, direction, number) :
    
    file_index = glob_vars.FILES.index(cur)
    
    if direction == 'left' :
        if file_index - number < 0 :
            return False
        return glob_vars.FILES[file_index - number]
        
    if direction == 'right' :
        if file_index + number > 7 :
            return False
        return glob_vars.FILES[file_index + number]


def get_depth(div, dic1, dic2) :
    
    return math.floor(div / (len(dic1)+len(dic2)))
