def findMinDistance(pointsList : list):
    disctOfNumbers = {}
    overallMin = None
    for index , item in enumerate(pointsList):
        if disctOfNumbers.get(item) is None:
            disctOfNumbers[item] = index
        else:
            numberIndex = disctOfNumbers[item]
            distance = index - numberIndex
            disctOfNumbers[item] = index
            if overallMin is None or distance < overallMin :
                overallMin = distance
    return overallMin

try:
    textInput = input()
    listOfinput = textInput.split(' ')
    numbersList = list(map(int, listOfinput))
    print(findMinDistance(numbersList))
except:
    print('Please enter numbers space-seperated')
    exit()