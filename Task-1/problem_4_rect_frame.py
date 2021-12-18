def makeLineFromWord(word: str , maxLength):
    whitespaces = ' '*(maxLength - len(word) - 4)
    print('* ' + word + whitespaces + ' *')

def printHeaderAndFooter(length : int):
    print('*'*(length))
    
def frameSentence(sentence : str):
    words = sentence.split(' ')
    maxLength = len(sorted(words, key=len)[-1]) + 4
    print(maxLength)
    printHeaderAndFooter(maxLength)
    for word in words:
        makeLineFromWord(word , maxLength)
    printHeaderAndFooter(maxLength)
    
    
sentence = input('Enter a sentece: ')
frameSentence(sentence)