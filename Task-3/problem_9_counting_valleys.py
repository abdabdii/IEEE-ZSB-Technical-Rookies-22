def countingValleys(steps):
    currentPosition = 0
    valleysCount = 0
    for step in steps:
        prevPosition = currentPosition
        if step == 'D':
            currentPosition -= 1
        elif step == 'U':
            currentPosition += 1
        if prevPosition == 0 and currentPosition == -1:
            valleysCount += 1
    return valleysCount



     
try:
    steps = int(input().strip())
    path = input()
    result = countingValleys(path)
    print(result)
except:
    print('Please enter valid numbers')
    exit()