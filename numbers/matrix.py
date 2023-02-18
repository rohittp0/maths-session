import timeit

import numpy as np


def multiply_matrix(A, B):
    result = np.zeros((A.shape[0], B.shape[1]))

    for i in range(len(A)):
        # iterating by column by B
        for j in range(len(B[0])):
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


def multiply_matrix_comprehension(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


def multiply_matrix_at(A, B):
    return A @ B

def multiply_matrix_numpy(A, B):
    return np.matmul(A, B)


M1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
])

M2 = np.array([
    [1, 2, 3, 5],
    [4, 5, 6, 7],
    [7, 8, 9, 9]
])

print(multiply_matrix_comprehension(M1, M2))







def bench_mark():
    timeit.timeit("multiply_matrix(M1, M2)", globals=locals())
    timeit.timeit("multiply_matrix_comprehension(M1, M2)", globals=locals())
    timeit.timeit("multiply_matrix_at(M1, M2)", globals=locals())
