n= int(input())
def Fib(n):
    fib1 = fib2 = 1

    n = n - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return fib2

print(Fib(n))