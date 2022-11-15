import numpy as np
from matrix import Matrix

class LU_Method(object):
    def __init__(self, a_matrix: Matrix, b_matrix: Matrix):
        self.a_matrix = a_matrix
        self.b_matrix = b_matrix
        self.l_matrix = None
        self.u_matrix = None

    def __find_LU(self):
        n = len(self.a_matrix.matrix)
        self.u_matrix = np.zeros((n, n))  # создаём нулевую матрицу перед вычислением U
        self.l_matrix = np.eye(n) # создаём единичную матрицу перед вычислением L
        self.u_matrix = Matrix(self.u_matrix)
        self.l_matrix = Matrix(self.l_matrix)

        for i in range(n):
            for j in range(n):
                if i <= j:
                    self.u_matrix[i][j] = self.a_matrix[i][j] - sum([self.l_matrix[i][k] * self.u_matrix[k][j] for k in range(i)])
                    if i == j and self.u_matrix[i][j] == 0:
                        raise "На главной диагонали U-матрицы присутствует 0. Матрица не может быть решена методом LU-разложения"
                if i > j:
                    self.l_matrix[i][j] = (self.a_matrix[i][j] - sum([self.l_matrix[i][k] * self.u_matrix[k][j] for k in range(j)])) / self.u_matrix[j][j]

    def find_x_vector(self):
        self.__find_LU()
        n = len(self.a_matrix.matrix)
        y_vector = [0 for i in range(n)]
        for i in range(n):
            y_vector[i] = self.b_matrix[i] - sum([self.l_matrix[i][k] * y_vector[k] for k in range(i)])
        y_vector = np.array(y_vector, dtype=np.float64)
        x_vector = [0 for i in range(n)]
        for i in reversed(range(n)):
            x_vector[i] = (y_vector[i] - sum([self.u_matrix[i][k] * x_vector[k] for k in range(i + 1, n)])) / self.u_matrix[i][i]
        x_vector = np.array(x_vector, np.float64)
        return x_vector, y_vector, self.l_matrix, self.u_matrix

    def find_reverse_matrix(self):
        if self.l_matrix is None or self.u_matrix is None:
            self.__find_LU()
        n = len(self.a_matrix.matrix)
        a_reverse = np.zeros((n, n), dtype=np.float64)
        old_b_matrix = self.b_matrix.matrix.copy()
        for i in range(n):
            b_vector = np.zeros(n, dtype=np.float64)
            b_vector[i] = 1
            self.b_matrix.matrix = np.array(b_vector, dtype=np.float64)
            x_vector, _, _, _ = self.find_x_vector()
            for j in range(n):
                a_reverse[j][i] = x_vector[j]

        self.b_matrix.matrix = old_b_matrix.copy()

        return Matrix(a_reverse)

    def find_determinant(self):
        if self.l_matrix is None or self.u_matrix is None:
            self.__find_LU()
        determinant = 1
        n = len(self.a_matrix.matrix)
        for i in range(n):
            determinant *= self.u_matrix[i][i]
        return determinant
