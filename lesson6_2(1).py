class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)


n = int(input())
array = []
while n != 0:
    ax, ay, az = map(int, input().split())
    A = Vector(ax, ay, az)
    B = A * A
    m = (B.x + B.y + B.z) ** (1 / 2)
    array.append(m)
    if m == max(array):
        V = A
    n -= 1
print(V.x, V.y, V.z)