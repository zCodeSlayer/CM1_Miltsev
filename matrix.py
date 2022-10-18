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

    def find_norm(self):
        n = len(self.matrix)
        norm = 0
        for i in range(n):
            summ = 0
            for j in range(n):
                summ += abs(self.matrix[i][j])
            if summ > norm:
                norm = summ
        return norm


