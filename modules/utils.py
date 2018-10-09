
FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def get_file(cur, direction) :
    
    global FILES
    
    file_index = FILES.index(cur)
    
    if file_index == 0 and direction == 'left' :
        return 'b'    
    if file_index == 7 and direction == 'right' :
        return 'g'
    if direction == 'left' :
        return FILES[file_index-1]
    if direction == 'right' :
        return FILES[file_index+1]
