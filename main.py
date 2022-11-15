from matrix import Matrix
from lu_method import LU_Method

def read_matrix_from_file(path):
    with open(path, 'r') as file:
        n = int(file.readline())
        a_matrix = list()
        b_matrix = list()
        for line in range(n):
            a_matrix.append([float(data) for data in file.readline().split()])
        for line in range(n):
            b_matrix.append(float(file.readline()))
    return a_matrix, b_matrix

def find_solve(A_matrix, B_matrix):
    a_matrix = Matrix(A_matrix.copy())
    b_vector = B_matrix.copy()
    b_matrix = Matrix(B_matrix.copy())

    lu_solve = LU_Method(a_matrix, b_matrix)
    x_vector, y_vector, l_matrix, u_matrix = lu_solve.find_x_vector()
    n = len(a_matrix.matrix)
    for i in range(n):
        summ = 0
        for j in range(n):
            summ += a_matrix[i][j] * x_vector[j]
        b_vector[i] -= summ

    print(f"A-матрица:\n{a_matrix}")
    print(f"L-матрица:\n{l_matrix}")
    print(f"U-матрица:\n{u_matrix}")
    print(f"Вектор y: {y_vector}")
    print(f"Вектор x: {x_vector}")
    print(f"Вектор невязок: {b_vector}")
    print(f"Определитель матрицы A: {lu_solve.find_determinant()}")

def find_reverse_matrix(matrix):
    a_matrix = Matrix(matrix.copy())
    lu_solve = LU_Method(a_matrix, Matrix([]))
    a_revers = lu_solve.find_reverse_matrix()
    return a_revers


if __name__ == '__main__':
    a_matrix, b_matrix = read_matrix_from_file("examples/ex_test_1.txt")
    find_solve(a_matrix, b_matrix)
    a_revers = find_reverse_matrix(a_matrix)
    a_matrix = Matrix(a_matrix.copy())
    a_norm = a_matrix.find_norm()
    a_revers_norm = a_revers.find_norm()
    condition_number = a_norm * a_revers_norm
    print(f"Обратная матрица: \n{a_revers}")
    print(f"Норма A: {a_norm}")
    print(f"Норма A(-1): {a_revers_norm}")
    print(f"Число обусловленности: {condition_number}")



