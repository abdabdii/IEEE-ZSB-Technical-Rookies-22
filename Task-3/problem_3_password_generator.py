from random import randrange , shuffle

passwordLength = 10
constraints = {'specialCharactersMinLength':1, 'numbersMinLength' : 1 , 'includeUpperCase': True}
specialCharacters = ['@', '#', '$','%', '&' ]


# This function takes lowerOrUpper param if True it is lower if false It's Upper default is lower
def generateLowerCaseOrUpperCase(length : int, lowerOrUpper = True ):
    charsAsciiRange = [97,123] if lowerOrUpper else [65,91]
    chars = []
    
    if length > 0:
        chars.append(chr(randrange(charsAsciiRange[0],charsAsciiRange[1])))
        currentChar = chr(randrange(charsAsciiRange[0],charsAsciiRange[1]))
        while len(chars) < length:
            chars.append(currentChar)
            currentChar = chr(randrange(charsAsciiRange[0],charsAsciiRange[1]))
    return chars

def generateAlphabetChars(length : int):
    if constraints['includeUpperCase']:
        lowerLength = randrange(1, length+1)
        upperLength = length - lowerLength
    else:
        lowerLength = length
        upperLength = 0
    lowerChars = generateLowerCaseOrUpperCase(lowerLength)
    upperChars =generateLowerCaseOrUpperCase(upperLength,False)
    return [*lowerChars,*upperChars]

def generateDigits(length : int):
    digits = []
    while len(digits) < length:
        digits.append(randrange(0,10))
    return digits

def generateSpecialChars(length : int):
    chars = []
    while len(chars) < length:
        index = randrange(0,len(specialCharacters))
        chars.append(specialCharacters[index])
    return chars

def generatePassword():
    charactersLengthUpperLimit = passwordLength - (constraints['numbersMinLength'] + constraints['specialCharactersMinLength'])
    charactersLength = 0 if charactersLengthUpperLimit == 0 else randrange(1,charactersLengthUpperLimit +1)
    specialCharactersLength = randrange(constraints['specialCharactersMinLength'],
                                        passwordLength - charactersLength - constraints['numbersMinLength'] + 1)
    digitsLength = passwordLength - charactersLength - specialCharactersLength    
    
    alphabetChars = []
    specialChars = []
    digits = []
    if charactersLength != 0:
        alphabetChars = generateAlphabetChars(charactersLength)
    if specialCharactersLength != 0:
        specialChars = generateSpecialChars(specialCharactersLength)
    if digitsLength != 0:
        digits = generateDigits(digitsLength)
    return [*alphabetChars ,*specialChars ,*digits]

password = list(map(str,generatePassword()))
shuffle(password)
print(''.join(password))
    
    
    
