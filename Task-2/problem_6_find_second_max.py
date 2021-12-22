def findMax(numbersList : list):
    maxValue = None
    for number in numbersList:
        if maxValue is None or number > maxValue:
            maxValue = number
    return maxValue


def findSecMax(numbersList : list):
    secondMax = findMax(numbersList)
    removedMax = list(filter(lambda a: a != secondMax, numbersList))
    return findMax(removedMax)

try:
    n = int(input())
    arr = list(map(int, input().split()))
    print(findSecMax(arr))
except:
    print('Please enter a valid numbers space-seperated')
    exit()