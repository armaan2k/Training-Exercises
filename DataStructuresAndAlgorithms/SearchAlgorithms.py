def linear_search(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index = index + 1
    return -1


A = [84, 21, 47, 96, 15]
found = linear_search(A, 100)
print("Result:", found)


def binary_search_iterative(A, key):
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            r = mid - 1
        elif key > A[mid]:
            l = mid + 1
    return -1


A = [15, 21, 47, 84, 96]
found = binary_search_iterative(A, 11)
print("Result:", found)


def binary_search_recursive(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search_recursive(A, key, l, mid - 1)
        elif key > A[mid]:
            return binary_search_recursive(A, key, mid + 1, r)


found = binary_search_recursive(A, 84, 0, 4)
print("Result:", found)
