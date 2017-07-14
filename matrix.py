import numpy

from vector import Vector3

class Matrix(object):
    @staticmethod
    @property
    def identity():
        return Matrix(numpy.eye(3))

    def __init__(self,
                 row1 = Vector3(1, 0, 0),
                 row2 = Vector3(0, 1, 0),
                 row3 = Vector3(0, 0, 1)):
        if  isinstance(row1, Vector3) and \
            isinstance(row2, Vector3) and \
            isinstance(row3, Vector3):

            self._matrix = numpy.array([row1.list, row2.list, row3.list])
        elif isinstance(row1, numpy.ndarray):
            self._matrix = row1

    def __str__(self):
        return str(self._matrix)

    def __getitem__(self, index):
        return Vector3(self._matrix[index][0],
                       self._matrix[index][1],
                       self._matrix[index][2])
    def __setitem__(self, index, value):
        #assert isinstance(value, Vector3)

        self._matrix[index] = value

    def __neg__(self):
        return Matrix(numpy.linalg.inv(self._matrix))

    def __mul__(self, other):
        assert isinstance(other, Matrix)

        return Matrix(self._matrix.dot(other._matrix))

