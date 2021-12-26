from math import floor , ceil

def pageCount(pages, target):
    midpoint = floor(pages/2)
    flips = None
    if target <= midpoint:
        if target % 2 == 0:
            flips = ceil(target/2)
        else:
            flips = floor(target/2)
    else:
        if pages % 2 == 0:
            flips = ceil((pages - target)/2) 
        else:
            flips = floor((pages - target)/2)   
    return flips
    
    
try:
    n = int(input().strip())
    p = int(input().strip())
    result = pageCount(n, p)
    print(result)
except:
    print('Please enter valid values')
    exit()
