def kaprekarNumbers(p, q):
    kaprekarNumbersList = []
    for number in range(p, q+1):
        digitsLength = len(str(number))
        squared = str(number*number)
        rightHand = squared[-digitsLength:]
        leftHand = squared[-len(squared):-digitsLength]

        comparingNumber = int(rightHand)
        if leftHand != '':
            comparingNumber += int(leftHand)
        if comparingNumber == number:
            kaprekarNumbersList.append(str(number))
    if not kaprekarNumbersList:
        print('INVALID RANGE')
    else:
        print(' '.join(kaprekarNumbersList))

# Can be checked at https://www.hackerrank.com/challenges/kaprekar-numbers/problem
