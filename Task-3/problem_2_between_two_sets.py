
def checkIfNumberPasses(a, b , possibleNumber, loopLength):
    for index in range(0,loopLength):
        if index < len(a):
            if possibleNumber % a[index] !=0:
                return False
        if index < len(b):
            if b[index] % possibleNumber !=0:
                return False
    return True

def getTotalX(a, b):
    possibleNumbers = []
    results=[]
    loopLength = len(a) if len(a) >= len(b) else len(b)
    minOfA = min(a)
    minOfB = min(b)
    minValue = minOfA if minOfA <= minOfB else minOfB
    possibleNumbers.append(max(a))
    possibleNumbers.extend(range(minValue, max(b) + 1))
    possibleNumbers = list(dict.fromkeys(possibleNumbers))
    for possibleNumber in possibleNumbers:
        passes = checkIfNumberPasses(a, b , possibleNumber, loopLength)
        if passes:
            results.append(possibleNumber)
    return len(results)
    



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)
print(total)

    
