import math

def isPrimeNumber(number : int):
    checkRange = math.floor(math.sqrt(number)) + 1
    for dividingNumber in range (1 , checkRange):
        if dividingNumber != 1:
            if number % dividingNumber == 0 :
                return ''
    return number
    
def getPrimeNumbers(numbersRange : int):
    primeNumbers = []
    for number in range (1, numbersRange + 1):
        primeNumbers.append(str(number)) if isPrimeNumber(number) != '' else None
    return primeNumbers

number = int(input('Please enter the number: '))
print(' '.join(getPrimeNumbers(number)))