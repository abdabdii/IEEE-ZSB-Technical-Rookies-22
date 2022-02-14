def bobAndString(S, T):
    operations = 0
    S = list(S)
    T = list(T)
    TLength = len(T)
    for letterS in S:
        matched = False
        idx = 0
        while not matched and idx < len(T):
            if T[idx] == letterS:
                del T[idx]
                matched = True
                break
            else:
                idx += 1
        if not matched:
            if TLength == len(S):
                operations += 1
            if TLength > len(S):
                operations += TLength - len(S)
                TLength = len(S)
            else:
                TLength += 1
            operations += 1

    return operations


for i in range(0, int(input())):
    S = input()
    T = input()
    print(bobAndString(S, T))


# Problem can be found at https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/bob-and-string-easy/description/
