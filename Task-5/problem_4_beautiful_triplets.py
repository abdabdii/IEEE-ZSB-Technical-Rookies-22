def beautifulTriplets(d, arr):
    triplets = 0
    for number in arr:
        newValue = number + d
        if newValue in arr:
            indexOfNext = arr.index(newValue)
            newValue2 = arr[indexOfNext] + d
            if newValue2 in arr:
                triplets += 1
    return triplets

# can be checked at https://www.hackerrank.com/challenges/beautiful-triplets/problem
