from random import randrange

def guessStatement(failedTries : int):
    if failedTries == 0:
        return ''
    elif failedTries == 1:
        return 'after 1 try'
    else:
        return 'after ' + str(failedTries) + ' tries'

def guessNumber():
    try:
        guessedNumber = int(input())
    except:
        print('Please enter a valid number')
        exit()
    return guessedNumber
    

def guessGame():
    failedTries = 0
    rightAnswer = randrange(1,11)
    guessedNumber = guessNumber()
    while rightAnswer != guessedNumber:
        failedTries += 1
        print('Wrong Answer ⛔')
        guessedNumber = guessNumber()
    print('Congratulations! your guess is right ✔️ ' + guessStatement(failedTries))
    exit()

guessGame()
    
    

    