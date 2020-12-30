#Example1
map(print, map(function, iterable))
#Task1
def get_cartesian_product(a,b):
    from itertools import product
    return list(map(tuple, product(a, b)))


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*get_cartesian_product(a, b))
#Task2
import itertools


def get_permutations(a, n):
    b = itertools.permutations(a, n)
    b = list(b)
    b.sort()
    return b


if __name__ == '__main__':
    s = input()
    n = int(input())
    v = get_permutations(s, n)
    for i in v:
        for j in range(n):
            print(i[j], end = "")
        print(" ", end = "")
#Task3
import itertools


def get_combinations(a, k):
    b = itertools.combinations(a, k)
    b = list(b)
    b.sort()
    return b


if __name__ == '__main__':
    m = []
    l = ""
    s = input()
    k = int(input())
    for y in range(1, k+1):
        v = get_combinations(s, y)
        for i in v:
            for j in range(y):
                l = str(l) + str(i[j])
            m.append(l)
            l = ""
    print(m)
#Task4
import itertools


def get_combinations_with_replacement(a, n):
    b = itertools.combinations_with_replacement(a, n)
    b = list(b)
    b.sort()
    return b


if __name__ == '__main__':
    s = input()
    n = int(input())
    v = get_combinations_with_replacement(s, n)
    for i in v:
        for j in range(n):
            print(i[j], end = "")
        print(" ", end = "")
#Task5
import itertools


def func(s):
    return hash(s)


def compress_string(s):
    arr = []
    b = itertools.groupby(s, key=func)
    for i, iter in b:
        a = list(iter)
        arr.append(a[0])
        arr.append(len(a))
        print(tuple(arr), end=" ")
        arr.pop()
        arr.pop()


if __name__ == '__main__':
    compress_string('12254477')
#Task6
import itertools


def maximize(lists, m):
    arr = []
    for i in lists:
        b = max(i)
        a = itertools.starmap(pow, [(b, 2)])
        a = list(map(int, a))
        a = int(a[0])
        arr.append(a)
    ar = list(itertools.accumulate(arr))
    v = ar.pop()
    print(v % m)


if __name__ == '__main__':
    lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
    maximize(lists, m=1000)