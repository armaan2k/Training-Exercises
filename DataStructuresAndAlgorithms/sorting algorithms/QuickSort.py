def quick_sort(A,low,high):
    if low < high:
        pi = partition(A, low, high)
        quick_sort(A, low, pi-1)
        quick_sort(A, pi + 1, high)

def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <= j and A[j] > pivot:
            j = j - 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


A = [3,5,8,9,6,2]
print('Original:', A)
quick_sort(A, 0, len(A)-1)
print('Sorted:', A)