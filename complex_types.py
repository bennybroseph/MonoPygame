from vector import Vector2, Vector3

class Size(Vector2):
    def __init__(self, w = 0, h = 0):
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
        self.y = float(value)

class Color(Vector3):
    def __init__(self, r = 255, g = 255, b = 255):
        Vector3.__init__(self, r, g, b)

    @property
    def r(self):
        return self.x
    @r.setter
    def r(self, value):
        self.x = float(value)

    @property
    def g(self):
        return self.y
    @g.setter
    def g(self, value):
        self.y = float(value)

    @property
    def b(self):
        return self.z
    @b.setter
    def b(self, value):
        self.z = float(value)

    @property
    def hsl(self):
        """Returns the r, g, and b values as hue, saturation, and brightness"""
        hsl = self.nomalized

        min_value = min(self.r, self.g, self.b)
        max_value = max(self.r, self.g, self.b)
        hsl.z = (min + max) / 2.0
        #TODO: Finish this function

    @property
    def hex(self):
        """Returns the r, g, and b values of the color into hexadecimal"""
        hex_values = [str(int(self.r // 16)),
                      str(int(self.r % 16)),
                      str(int(self.g // 16)),
                      str(int(self.g % 16)),
                      str(int(self.b // 16)),
                      str(int(self.b % 16))]

        hex_letters = ["A", "B", "C", "D", "E", "F"]
        result = "0x"
        for i in range(0, len(hex_values)):
            int_value = int(hex_values[i])
            if int_value > 9:
                hex_values[i] = hex_letters[int_value - 10]

            result += hex_values[i]

        result = int(result, 16)
        result = hex(result)
        return result

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

