def palindrome(word : str):
    index = len(word) -1
    reversedArr = []
    while index >= 0:
        reversedArr.append(word[index])
        index -=1
    reversedWord = ''.join(reversedArr)
    return 'yes' if reversedWord == word else 'no'
    
        
word = input()
print(palindrome(word))
        