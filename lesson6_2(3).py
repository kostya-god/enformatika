class Vector():

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __matmul__(self, other):
        return Vector(self.y * other.z - self.z * other.y, -(self.x * other.z - self.z * other.x), self.x * other.y - self.y * other.x)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)


ax, ay, az = map(int, input().split())
bx, by, bz = map(int, input().split())
cx, cy, cz = map(int, input().split())
A = Vector(ax, ay, az)
B = Vector(bx, by, bz)
C = Vector(cx, cy, cz)
D = A @ B
E = C * D
S = (D.x * D.x + D.y * D.y + D.z * D.z)**(1/2)
V = (E.x + E.y + E.z)/3
print("Площадь параллелограмма, натянутого на вектора A и В =", S)
print("Объём параллелепипеда, натянутого на вектора A, В, С =", V)