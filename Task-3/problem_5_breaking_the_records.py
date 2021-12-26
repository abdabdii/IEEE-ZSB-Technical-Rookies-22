def breakingRecords(scores):
    recordBreaking = [0,0]
    currentHighest = scores[0]
    currentLowest = scores[0]
    for score in scores:
        if score > currentHighest:
            currentHighest = score
            recordBreaking[0] += 1
        if score < currentLowest:
            currentLowest = score
            recordBreaking[1] += 1
    return recordBreaking
    
try:
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)
except:
    print('Please enter a valid list of scores')
    exit()

