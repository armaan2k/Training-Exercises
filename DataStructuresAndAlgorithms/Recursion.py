# iterative function
def calculate_itr(n):
    while n > 0:
        k = n ** 2
        print(k)
        n = n - 1


# recursive function
def calculate_rec(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate_rec(n - 1)


calculate_rec(4)
calculate_itr(4)

print("\n____________________________________________________________________________________\n")


# sum of N numbers
def sum_rec(n):
    if n == 0:
        return 0
    return sum_rec(n - 1) + n


print(sum_rec(4))


# Factorial
def factorial_rec(n):
    if n == 0:
        return 1
    return factorial_rec(n - 1) * n


print(factorial_rec(5))
