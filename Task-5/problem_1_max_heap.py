def left(inedx):
    return 2 * inedx + 1


def right(inedx):
    return 2 * inedx + 2


def max_heapify(A, index):
    l = left(index)
    r = right(index)
    if l < len(A) and A[l] > A[index]:
        largest = l
    else:
        largest = index
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)


def build_max_heap(A):
    n = int((len(A)//2)-1)
    for index in range(n, -1, -1):
        max_heapify(A, index)


A = [81, 13, 77, 24, 35, 61, 48, 3, 23, 87,
     92, 95, 74, 57, 99, 86, 28, 15, 55, 7, 51]
build_max_heap(A)
print(A)
