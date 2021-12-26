
def kangaroo(x1, v1, x2, v2):
    while x1 <= x2 and v1 > v2:
        if x1 == x2:
            return 'YES'
        else:
            x1 += v1
            x2 += v2
    return 'NO'


try:
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    print(kangaroo(x1, v1, x2, v2))
except:
    print('Please enter valid numbers')
    exit()
