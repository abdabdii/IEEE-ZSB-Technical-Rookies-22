def minDistance(numbersList: list):
    numbers = {}
    minDistance = None
    for index, number in enumerate(numbersList):
        if not numbers.get(number):
            numbers[number] = [index, 0]
            continue
        currentMin = index - numbers[number][0]
        if minDistance:
            if minDistance > currentMin:
                minDistance = currentMin
        else:
            minDistance = currentMin
        numbers[number] = [index, currentMin]
    return minDistance


try:
    inputText = input()
    inputList = inputText.split(' ')
    print(minDistance(inputList))
except:
    print('Please enter text seperated by spaces')
    exit()
