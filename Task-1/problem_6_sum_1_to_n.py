def sum1ToN(number : int):
    sum = 0
    while number >= 1:
        sum += number
        number -= 1
    return sum


try:
    number = int(input('Please enter a number: '))
    print(sum1ToN(number))
except:
    print('Please enter a valid number')
    exit()