import sys
n= int(input())
def Fib(n):
    fib1 = fib2 = 1

    n = n - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return fib2
if __name__ == "__main__":
    if len (sys.argv) == 1:
        print(Fib(n))
    else:
        if len(sys.argv) == 2:
            if sys.argv[1] == '-n':
                print(Fib(n))
            else:
                print('Unvalid argument')
                sys.exit(1)
        else:
            print('Incorrect number of arguments')
            sys.exit(1)




