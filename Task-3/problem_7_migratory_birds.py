def migratoryBirds(arr):
    occurrances = [0]*5
    result = None
    for sighting in arr:
        occurrances[sighting -1] += 1

    maxOccurance = max(occurrances)
    for index , occur in enumerate(occurrances):
        if occur == maxOccurance:
            result = index+1
            break
    return result
       
try:
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
except:
    print('Please enter a valid list of integars')
    exit()
