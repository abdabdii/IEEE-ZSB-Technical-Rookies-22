def countSubString(string, sub_string):
    subStringLength = len(sub_string)
    stringLength = len(string)
    stringList = list(string)
    subStringList = list(sub_string)
    occurences = 0
    for index in range(0, stringLength):
        if index + subStringLength -1 <=  stringLength:
            if stringList[index: index + subStringLength] == subStringList:
                occurences += 1
    return occurences

originalText = input('Please enter the string: \n')
subStringText = input('Please enter the sub string: \n')
print(countSubString(originalText, subStringText))
