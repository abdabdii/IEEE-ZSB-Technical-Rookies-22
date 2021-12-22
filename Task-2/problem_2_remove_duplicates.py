def removeDuplicated(listInput : list):
    nonDuplicated = {}
    nonDuplicatedList = []
    for item in listInput:
        nonDuplicated[item] = item
    for nonDuplicatedItem in nonDuplicated:
        nonDuplicatedList.append(nonDuplicatedItem)
    return nonDuplicatedList
    
try:
    inputText = input()
    inputList = inputText.split(' ')
    print(' '.join(removeDuplicated(inputList)))
except:
    print('Please enter text seperated by spaces')
    exit()
    
    