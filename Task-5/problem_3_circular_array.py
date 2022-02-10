def circularArrayRotation(a, k, queries):
    indiciesValues = []
    for i in range(0, k):
        a.insert(0, a.pop())
    for query in queries:
        indiciesValues.append(a[query])

    return indiciesValues

# Problem at https://www.hackerrank.com/challenges/circular-array-rotation/problem
