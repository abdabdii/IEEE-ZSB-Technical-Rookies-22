import sys
sys.path.append('../')
from helpers import test


def sumUsingFor(numbers : list[float]):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def sumUsingWhile(numbers : list[float]):
    sum = 0
    while len(numbers) > 0:
        sum += numbers.pop()
    return sum

def sumUsingRecursive(numbers: list[float], sum = 0):
    if len(numbers) == 0:
        return sum
    else:
        sum += numbers.pop()
        return sumUsingRecursive(numbers,sum)
    


#Testing section start
test1 = [1,2,4,7,9,23,44]
test2 = [1.25,2.632,3.64541]
test3 = []

test(sumUsingFor(test1) == 90 and sumUsingRecursive(test1.copy()) == 90 and sumUsingWhile(test1.copy()) == 90 , 'Test integars')
test(sumUsingFor(test2) ==  sumUsingRecursive(test2.copy()) ==  sumUsingWhile(test2.copy()) , 'Test Floats')
test(sumUsingFor(test3) == 0 and sumUsingRecursive(test3.copy()) == 0 and sumUsingWhile(test3.copy()) == 0 , 'Test empty')
#Testing section end

try:
    numbersLimit = int(input())
except:
    print('Please enter valid number')
    exit()

numbersList = input().split(' ')
if len(numbersList) == numbersLimit:
    numbersList = list(map(int, numbersList))
    print(sumUsingFor(numbersList.copy()))
    print(sumUsingWhile(numbersList.copy()))
    print(sumUsingRecursive(numbersList.copy()))
else:
    print('Please enter valid numbers with length of N space-seperated')
    exit()

