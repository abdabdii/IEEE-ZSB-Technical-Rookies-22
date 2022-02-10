def numberOfR(sequence: str, n):
    text = sequence
    while len(text) < n:
        text += sequence
    return text[0:n].count('r')


print(numberOfR('rar', 10))
