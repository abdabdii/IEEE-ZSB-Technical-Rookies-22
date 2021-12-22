import sys
sys.path.append('../')
from helpers import test
from random import randrange


# this variable is responsible for controlling how long the generated number is.
digitsLength = 3


def getResults(guessedNumber : int, correctNumber : int):
    hitsAndMisses = {'hits':0 , 'miss':0}
    guessedNumberStr = str(guessedNumber)
    correctNumberStr = str(correctNumber)
    correctNumberArr = [digit for digit in correctNumberStr]
    
    for index, digit in enumerate(guessedNumberStr):
        if correctNumberStr[index] == digit:
            hitsAndMisses['hits'] += 1
            correctNumberArr[index] = None
       
    for digit in guessedNumberStr:
        if digit in correctNumberArr:
            hitsAndMisses['miss'] += 1
        
    return hitsAndMisses

#Test getResults function section START

test1 = getResults(413,427)
test2 = getResults(412,427)
test3 = getResults(444,555)
test4 = getResults(123,312)
test5 = getResults(555,555)

test(test1['hits'] == 1 and test1['miss'] == 0, 'Test case 1. 1 hit and zero misses')
test(test2['hits'] == 1 and test2['miss'] == 1, 'Test case 2. 1 hit 1 miss')
test(test3['hits'] == 0 and test3['miss'] == 0, 'Test case 3. 0 hit 0 miss')
test(test4['hits'] == 0 and test4['miss'] == 3, 'Test case 4. 0 hit 3 misses')
test(test5['hits'] == 3 and test5['miss'] == 0, 'Test case 5. 3 hits 0 miss')



#Test getResults function section END


def generatePluralOrSingular(number : int ,text : str):
    if number <= 1:
        return text
    else:
        if text[-1] == 's':
            return text + 'es'
        else:
            return text + 's'

def generateStatement(hitsAndMisses : dict):
    hits = hitsAndMisses['hits']
    miss = hitsAndMisses['miss']
    return str(hits) + ' ' + generatePluralOrSingular(hits , 'hit') + ' ' + str(miss) + ' ' + generatePluralOrSingular(miss , 'miss')

def numberInput():
    try:
        numberStr = input()
        int(numberStr)
        if len(numberStr) != digitsLength:
            print('Please enter a '+ digitsLength +' digit number')
            exit()
        return numberStr
    except:
        print('Please enter a valid number')
        exit()
        
def intializeGame():
    correctAnswer = randrange(pow(10,digitsLength-1),pow(10,digitsLength))
    # Remove this line if you want to hide the correct answer
    print(correctAnswer)
    guessedNumber = numberInput()
    hitsAndMiss = getResults(int(guessedNumber) , correctAnswer)
    print(generateStatement(hitsAndMiss))
    while hitsAndMiss['hits'] != digitsLength:
        guessedNumber = numberInput()
        hitsAndMiss = getResults(guessedNumber , correctAnswer)
        print(generateStatement(hitsAndMiss))
    print('Congrats you nailed it! the answer is ' + str(correctAnswer))
    exit()

intializeGame()