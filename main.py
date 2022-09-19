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
    b_matrix = Matrix(B_matrix.copy())

    lu_solve = LU_Method(a_matrix, b_matrix)
    x_vector, y_vector, l_matrix, u_matrix = lu_solve.find_x_vector()
    print(f"L-матрица:\n{l_matrix}")
    print(f"U-матрица:\n{u_matrix}")
    print(f"Вектор y: {y_vector}")
    print(f"Вектор x: {x_vector}")

def find_reverse_matrix(matrix):
    pass

if __name__ == '__main__':
    a_matrix, b_matrix = read_matrix_from_file("examples/test.txt")
    find_solve(a_matrix, b_matrix)


