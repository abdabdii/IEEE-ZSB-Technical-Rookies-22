def getMoneySpent(keyboards, drives, b):
    listOfPrices = []
    for keyboard in keyboards:
        if keyboard < b:
            for drive in drives:
                if keyboard + drive <= b:
                    listOfPrices.append(keyboard+drive)
    if len(listOfPrices) <= 0:
        return -1
    listOfPrices.sort(reverse=True)
    return listOfPrices[0]


#Check problem at https://www.hackerrank.com/challenges/electronics-shop/problem
