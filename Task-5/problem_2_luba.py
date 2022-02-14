import sys
sys.path.append('../')
from helpers import test


def minDays(timeRequired, listOfDays):
    currentFreeTime = 0
    for idx, time in enumerate(listOfDays):
        currentFreeTime += 86400 - time
        if currentFreeTime >= timeRequired:
            return idx + 1


test1 = minDays(2, [86400, 86398])
test2 = minDays(86400, [0, 86400])

test(test1 == 2, 'Test case 1 : \n 2 2 \n 86400 86398')
test(test2 == 1, 'Test case 2 : \n 2 86400 \n 0 86400')

listOfNumbers = input(
    "Enter number of day and time required to finish reading: ").rstrip().split()
timeOfDays = input(
    "Enter the work time of Luba: ").rstrip().split()
timeOfDays = list(map(int, timeOfDays))
