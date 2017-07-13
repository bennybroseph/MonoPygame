import numpy

from vector import Vector3

class Matrix(object):
    def __init__(self,
                 row1 = Vector3(1, 0, 0),
                 row2 = Vector3(0, 1, 0),
                 row3 = Vector3(0, 0, 1)):
        assert(row1, Vector3)
        assert(row2, Vector3)
        assert(row3, Vector3)

        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

