import sys
import argparse
def Fib(n):
    fib1 = fib2 = 1
    n = n - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return fib2
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', nargs='?')
    parser.add_argument ('name', nargs='?')
    return parser
if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if len (sys.argv) == 2:
        print(Fib(int(namespace.name)))
    else:
        print(Fib(int(namespace.n)))






