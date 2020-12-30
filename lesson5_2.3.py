class Animal:

    def __init__(self, name, age):
        self.n = name
        self.a = age

    def __str__(self):
        return str(self.n) + " " + str(self.a)


class Zebra(Animal):

    def __str__(self):
        return super().__str__() + " " + 'This animal is zebra'


class Dolphin(Animal):

    def __str__(self):
        return super().__str__() + " " + 'This animal is dolphin'


print("Write name and age of animal")
name = input()
age = int(input())
print("Write 'z' if animal is zebra or write 'd' if animal is dolphin")
animal = input()
an = Animal(name, age)
d = Dolphin(name, age)
z = Zebra(name, age)
if animal == "d":
    print(d)
elif animal == "z":
    print(z)
else:
    print("This animal isn't zebra or dolphin")