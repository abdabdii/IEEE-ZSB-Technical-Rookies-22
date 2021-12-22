def diagonalDifference(arr :list , size : int):
    difference = 0
    for index, subArr in enumerate(arr):
        difference = difference + subArr[index] - subArr[size-index-1]
    return abs(difference)

n = int(input().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr, n)
print(result)