def insertionSort(unsortedList : list):
    sortedList = [None] * len(unsortedList)
    for index, value in enumerate(unsortedList):
        while(index > 0 and sortedList[index - 1] > value):
            sortedList[index] = sortedList[index - 1]
            index = index -1
        sortedList[index] = value
    return sortedList

print(insertionSort([5,4,5,6,9,2,1,7]))
        