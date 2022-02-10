def chocolateFeast(n, c, m):
    numberOfChoco = n / c
    numberOfWrappers = numberOfChoco
    while numberOfWrappers >= m:
        numberOfWrappers -= m
        numberOfChoco += 1
        numberOfWrappers += 1
    return int(numberOfChoco)


# can be tested at https://www.hackerrank.com/challenges/chocolate-feast/problem
