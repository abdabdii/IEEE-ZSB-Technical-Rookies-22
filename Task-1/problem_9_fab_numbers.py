def fabNumbers(number : int):
    numbers = [0,1]
    currentIndex = 2
    while (len(numbers) < number):
        numbers.append(numbers[currentIndex-2] + numbers[currentIndex-1])
        currentIndex +=1
    return numbers
    
        
try:
    number = int(input())
    print(fabNumbers(number))
except:
    print('Please enter a valid number')
    exit()