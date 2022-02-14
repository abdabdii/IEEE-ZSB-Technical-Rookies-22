from numpy import number


def deleteFriends(numberToDelete, popList):
    index = 0
    while index < len(popList)-1 and numberToDelete > 0:
        if int(popList[index]) < int(popList[index+1]):
            del popList[index]
            numberToDelete -= 1
        else:
            index += 1
    while numberToDelete > 0:
        popList.pop(0)
        numberToDelete -= 1
    return popList


testCases = input("enter test cases:").rstrip()
for i in range(0, int(testCases)):
    listOfNumbers = input(
        "enter number of friends and how many you want to delete:").rstrip().split()
    popularityList = input(
        "enter the popularity of each friend space seperated:").rstrip().split()
    print(deleteFriends(int(listOfNumbers[1]), popularityList))


# Problem can be found at https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/remove-friends-5/
