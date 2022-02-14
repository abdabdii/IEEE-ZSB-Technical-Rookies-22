def hackerrankInString(s):
    hackerRank = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    for letter in s:
        if len(hackerRank) > 0 and letter == hackerRank[0]:
            hackerRank.pop(0)
    if len(hackerRank) == 0:
        return 'YES'
    return 'NO'


# Problem can be found at https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
