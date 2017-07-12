import math
import numbers

class Vector2(object):
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        assert isinstance(other, Vector2)

        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return type(self)(-self.x, -self.y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return type(self)(self.x + other.x, self.y + other.y)

        assert isinstance(other, numbers.Number)

        return type(self)(self.x + float(other), self.y + float(other))
    def __radd__(self, other):
        return self + other
    def __iadd__(self, other):
        self = self + other

    def __sub__(self, other):
        return self + (-other)
    def __sub__(self, other):
        self = self - other

    def __mul__(self, other):
        assert(other, numbers.Number)

        return type(self)(self.x * float(other), self.y * float(other))
    def __imul__(self, other):
        self = self * other

    def __truediv__(self, other):
        assert isinstance(other, numbers.Number)

        return type(self)(self.x / float(other), self.y / float(other))
    def __idiv__(self, other):
        self = self / other

    @property
    def magnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))
    @property
    def nomalized(self):
        if self.magnitude == 0.0:
            return self

        return type(self)(self.x / self.magnitude, self.y / self.magnitude)

    @property
    def tuple(self):
        return (self.x, self.y)

    @staticmethod
    def scale(a, b):
        assert isinstance(a, Vector2) and isinstance(b, Vector2)

        return type(a)(a.x * b.x, a.y * b.y)

class Vector3(object):
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __eq__(self, other):
        assert isinstance(other, Vector2)

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self):
        return type(self)(-self.x, -self.y, -self.z)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return type(self)(self.x + other.x, self.y + other.y, self.z + other.z)

        assert isinstance(other, numbers.Number)

        return type(self)(self.x + float(other),
                          self.y + float(other),
                          self.z + float(other))
    def __radd__(self, other):
        return self + other
    def __iadd__(self, other):
        self = self + other

    def __sub__(self, other):
        return self + (-other)
    def __sub__(self, other):
        self = self - other

    def __mul__(self, other):
        assert(other, numbers.Number)

        return type(self)(self.x * float(other),
                          self.y * float(other),
                          self.z * float(other))
    def __imul__(self, other):
        self = self * other

    def __truediv__(self, other):
        assert isinstance(other, numbers.Number)

        return type(self)(self.x / float(other),
                          self.y / float(other),
                          self.z / float(other))
    def __idiv__(self, other):
        self = self / other

    @property
    def magnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))
    @property
    def nomalized(self):
        if self.magnitude == 0.0:
            return self

        return type(self)(self.x / self.magnitude,
                          self.y / self.magnitude,
                          self.z / self.magnitude)

    @property
    def tuple(self):
        return (self.x, self.y, self.z)

    @staticmethod
    def scale(a, b):
        assert isinstance(a, Vector2) and isinstance(b, Vector2)

        return type(a)(a.x * b.x, a.y * b.y)
