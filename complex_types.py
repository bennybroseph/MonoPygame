import numbers

class Vector2(object):
    def __init__(self, x, y):
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

    @staticmethod
    def scale(a, b):
        assert isinstance(a, Vector2) and isinstance(b, Vector2)

        return type(a)(a.x * b.x, a.y * b.y)

class Size(Vector2):
    def __init__(self, w, h):
        Vector2.__init__(self, w, h)

    @property
    def w(self):
        return self.x
    @w.setter
    def w(self, value):
        self.x = float(value)

    @property
    def h(self):
        return self.y
    @h.setter
    def h(self, value):
        self.h = float(value)

class Bounds(object):
    def __init__(self, center = Vector2(0.0, 0.0), size = Size(1.0, 1.0)):
        assert isinstance(center, Vector2)
        assert isinstance(size, Size)

        self.center = center
        self.size = size

    @property
    def extents(self):
        return self.size / 2
    @extents.setter
    def extents(self, value):
        assert isinstance(value, Size)

        self.size = value * 2

    @property
    def min(self):
        return Vector2(self.center.x - self.extents.w, 
                       self.center.y - self.extents.h)
    @min.setter
    def min(self, value):
        assert isinstance(value, Vector2)

        self.size = Size(self.max.x - value.x, self.max.y - value.y)
        self.center = Vector2(value.x + self.extents.w, value.y + self.extents.h)

    @property
    def max(self):
        return Vector2(self.center.x + self.extents.w, 
                       self.center.y + self.extents.h)
    @max.setter
    def max(self, value):
        assert isinstance(value, Vector2)

        self.size = Size(value.x - self.min.x, value.y - self.min.y)
        self.center = Vector2(value.x - self.extents.w, value.y - self.extents.h)

