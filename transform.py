from vector import Vector3
from component import Component

class Transform(Component):
    def __init__(self):
        Component.__init__(self)

        localMatrix = (Vector3(),
                       Vector3(),
                       Vector3())

