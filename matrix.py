import numpy as np

class Matrix(object):
    def __init__(self, matrix: list):
        self.matrix:np.ndarray = np.array(matrix, dtype=np.float64)

    def __mul__(self, other_matrix):
        return Matrix(self.matrix.dot(other_matrix.matrix))

    def __getitem__(self, index: int):
        return self.matrix[index]

    def __setitem__(self, index: int, value: float | int):
        self.matrix[index] = value

    def __str__(self):
        return f"{self.matrix}"