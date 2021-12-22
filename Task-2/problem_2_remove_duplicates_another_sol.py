def removeDuplicatesSortedList(sortedList : list):
    sortedListNoDuplicates = [sortedList[0]] if len(sortedList) > 0 else []
    for item in sortedList:
        if item > sortedListNoDuplicates[-1]:
            sortedListNoDuplicates.append(item)
    return sortedListNoDuplicates
        
try:
    inputText = input()
    inputList = inputText.split(' ')
    print(' '.join(removeDuplicatesSortedList(inputList)))
except:
    print('Please enter text seperated by spaces')
    exit()