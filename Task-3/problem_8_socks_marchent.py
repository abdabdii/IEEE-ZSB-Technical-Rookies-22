def sockMerchant(n, socks):
    socksAsDict = {}
    pairsOfSocks = 0
    
    for sock in socks:
        if sock in socksAsDict:
            socksAsDict[sock] += 1
        else:
            socksAsDict[sock] = 1
            
        if socksAsDict[sock] == 2:
            pairsOfSocks += 1
            socksAsDict[sock] = 0
    return pairsOfSocks

try:
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
except:
    print('please enter a valid integars')
    exit()
