import sys
sys.path.append('../')
from helpers import test

# This variable controls how many bottles you want to fill
fillableBottles = 2

def getMaxCapacity(bottlesCapacities : list):
    bottlesCapacitiesCopy = bottlesCapacities.copy()
    maxCapacity = 0
    for _ in range(0, fillableBottles):
        currentMax = max(bottlesCapacitiesCopy)
        maxCapacity += currentMax
        if currentMax in bottlesCapacitiesCopy: bottlesCapacitiesCopy.remove(currentMax)
    return maxCapacity
        
#Test section for getMaxCapacity Function START      
test1 = [2,3,5,9,6,8]
test2 = [5,5,5,5]

test(getMaxCapacity(test1) == 17, 'Test Case 1. [2,3,5,9,6,8]')
test(getMaxCapacity(test2) == 10, 'Test Case 2. list of fives')
#Test section for getMaxCapacity Function END

bottlesRemainingWater = []
bottlesCapacities = []

try:
    for _ in range(int(input())):
            lineInput = input().split(' ')
            bottlesRemainingWater.append(int(lineInput[0]))
            bottlesCapacities.append(int(lineInput[1]))
except:
    print('Please enter valid numbers')
    exit()

isBottleBigEnough = sum(bottlesRemainingWater) <= getMaxCapacity(bottlesCapacities)

print('Yes' if isBottleBigEnough else 'No')


    