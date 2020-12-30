#Task1
from random import randint
a = []
n = int(input())
for i in range(n):
    a.append(randint(0, 1991))

for i in a:
    a[0] = 6

print(a)
print('Возможно')
#Task2
class BinTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinTree(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinTree(value)
                else:
                    self.right.add(value)
        else:
            self.value = value

    def DFS(self, root):
        res = []
        if root:
            res = self.DFS(root.left)
            res.append(root.value)
            res = res + self.DFS(root.right)

        return res

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()


if __name__ == "__main__":
    tree = BinTree(5)
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.PrintTree()
#Task3
from zipfile import ZipFile
import os
import string
import shutil


class TextLoader(ZipFile):

    def __init__(self, file, path):
        super().__init__(file)
        self.file_in_dir = None
        self.extractall(path)
        self.path = path
        self.path_of_file = path + "\\sample\\"
        self.iter = iter(os.listdir(self.path_of_file))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __len__(self):
        file_count = len(os.listdir(self.path_of_file))
        return file_count

    def __iter__(self):
        return self

    def __del__(self):
        shutil.rmtree(self.path)

    def __next__(self):
        self.file_in_dir = next(self.iter)
        file = self.path_of_file + self.file_in_dir
        a = []
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                l = line.translate(str.maketrans('', '', string.punctuation))
                l = l.lower()
                a.append(l)

        with open(file, 'w', encoding='utf8') as f:
            f.writelines(a)

        f = open(file, 'r', encoding='utf8')
        return f


if __name__ == "__main__":
    where_from = r'C:/Users/ovsy2/Downloads/sample.zip'
    where_to = r'C:\Users\ovsy2\PycharmProjects\untitled2\lab9\hz'
    text_loader = TextLoader(where_from, where_to)
    print(len(text_loader))
    counter = 0
    for file in text_loader:
        counter += 1
    print(counter)
#Task4
import numpy as np
from random import randint


class PrintVariance(Exception):
    pass


class PrintMean(Exception):
    pass


class PrintCount(Exception):
    pass


def server_coroutine():
    aggregator = []
    try:
        while True:
            try:
                to_add = yield
                aggregator.append(to_add)
            except PrintVariance:
                yield np.var(aggregator)
            except PrintMean:
                yield np.mean(aggregator)
            except PrintCount:
                yield len(aggregator)
    finally:
        pass


if __name__ == "__main__":

    coroutine = server_coroutine()
    next(coroutine)

    for i in range(randint):

        coroutine.send(i)

        print( coroutine.throw(PrintVariance))
        next(coroutine)

        print(coroutine.throw(PrintMean))
        next(coroutine)

        print(coroutine.throw(PrintCount))
        next(coroutine)

    coroutine.close()
#Task5
class Connect(Exception):
    pass


class Write(Exception):
    pass


def connect_user(user_info):
    pass  # doing smth with info
    # command_planner().throw(Write)
    with open("file.txt", 'w') as f:
        yield from write_to_file(f)


def write_to_file(f_obj):
    while True:
        x = yield
        if x == "Stop":
            break
        f_obj.writelines(x)
        f_obj.writelines("\n")
    f_obj.close()


def command_planner():
    print("Work has started")
    auth = []
    while True:
        try:
            info = yield
            auth.append(info)
        except Connect:
            yield from connect_user(auth)


if __name__ == "__main__":
    coroutine = command_planner()
    next(coroutine)
    coroutine.send(["Dmitriy", "Ovsiy"])
    next(coroutine)
    coroutine.throw(Connect)
    coroutine.send("info")
    coroutine.send("something")
    coroutine.send("stop")

    coroutine.close()
    