from vector import Vector2, Vector3
from matrix import Matrix
from component import Component

class Transform(Component):
    def __init__(self):
        Component.__init__(self)

        self.localMatrix = Matrix()

    @property
    def up(self):
        return Vector2(self.localMatrix[1].x, self.localMatrix[1].y)
    @property
    def down(self):
        return -self.up

    @property
    def right(self):
        return Vector2(self.localMatrix[0].x, self.localMatrix[0].y)
    @property
    def left(self):
        return -self.right

    @property
    def position(self):
        return Vector2(self.localMatrix[2].x, self.localMatrix[2].y)
    @position.setter
    def position(self, value):
        assert isinstance(value, Vector2)

        self.localMatrix[2] = [value.x, value.y, 1.0]

