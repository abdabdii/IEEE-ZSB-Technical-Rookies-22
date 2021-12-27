import sys
sys.path.append('../')
from helpers import test

def addZeros(digitsList : list):
    zeros =  [0]*(4 - len(digitsList))
    return [*zeros ,*digitsList]


def transformNumber(number : int):
    numbersList = list(map(int, str(number)))
    if len(numbersList) < 4 :
        numbersList = addZeros(numbersList)
    ascendingNumbers = ''.join(map(str , sorted(numbersList)))
    decendingNumbers = ''.join(map(str,sorted(numbersList , reverse=True)))
    return abs(int(ascendingNumbers) - int(decendingNumbers))

def intializeSolution(number : int):
    tries = 0
    while number != 6174:
        tries += 1
        number = transformNumber(number)
    return tries

# Test section START
test(intializeSolution(2111) == 5, 'Test Case 1. testing 2111')
test(intializeSolution(9831) == 7, 'Test Case 2. testing 9831')
test(intializeSolution(6174) == 0, 'Test Case 3. testing 6174')
# Test section END

try:
    number = int(input())
    print(intializeSolution(number))
except:
    print('Please enter a valid number')
    exit()