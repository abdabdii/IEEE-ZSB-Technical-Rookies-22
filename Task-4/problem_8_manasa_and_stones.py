def addValue(value, checkList):
    if value not in checkList:
        checkList.append(value)


def stones(n, a, b):
    currentLevel = 1
    stonesList = [[0]]
    print(stonesList)
    while currentLevel < n:
        currentStoneList = []
        for possibleStone in stonesList[currentLevel - 1]:
            firstValue = possibleStone + a
            secondValue = possibleStone + b
            addValue(firstValue, currentStoneList)
            addValue(secondValue, currentStoneList)
        stonesList.append(currentStoneList)
        currentLevel += 1
    stonesList[-1].sort()
    return stonesList[-1]


# Can be checked at https://www.hackerrank.com/challenges/manasa-and-stones/problem
