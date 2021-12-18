import math

def binarySearch(searchArray : list , searchTarget : float):
    startingPointer = 0
    endingPointer = len(searchArray) -1
    
    while(startingPointer <= endingPointer):
        midpoint = math.floor((startingPointer+endingPointer)/2)
        if searchArray[midpoint] == searchTarget:
            return midpoint
        elif searchTarget > searchArray[midpoint]:
            startingPointer = midpoint +1
        else:
            endingPointer = midpoint -1
    return 'Not Found'
    
    
    
    
    
    
        
print(binarySearch([1,2,3,4,5,6],5))
