def add_matrices(mat_1, mat_2):
    """Adds two matrices"""
    if len(mat_1) == 1:
        return [[mat_1[0][0] + mat_2[0][0]]]
    n = len(mat_1)
    return [[mat_1[i][j] + mat_2[i][j] for j in range(n)] for i in range(n)]


def subtract_matrices(mat_1, mat_2):
    """Subtract two matrices"""
    if len(mat_1) == 1:
        return [[mat_1[0][0] - mat_2[0][0]]]
    n = len(mat_1)
    return [[mat_1[i][j] - mat_2[i][j] for j in range(n)] for i in range(n)]


def strassen_mult(mat_X, mat_Y):
    """Strassen's algorithm for 2n x 2n matrix multiplcation"""
    if len(mat_X) == 1:
        return [[mat_X[0][0] * mat_Y[0][0]]]

    m = len(mat_X[0])
    n = m // 2

    # Define submatrices in terms of four quadrants of cartesian plane
    quad1_X = [[mat_X[i][j] for j in range(n, 2 * n)] for i in range(n)]
    quad2_X = [[mat_X[i][j] for j in range(n)] for i in range(n)]
    quad3_X = [[mat_X[i][j] for j in range(n)] for i in range(n, 2 * n)]
    quad4_X = [[mat_X[i][j] for j in range(n, 2 * n)] for i in range(n, 2 * n)]
    quad1_Y = [[mat_Y[i][j] for j in range(n, 2 * n)] for i in range(n)]
    quad2_Y = [[mat_Y[i][j] for j in range(n)] for i in range(n)]
    quad3_Y = [[mat_Y[i][j] for j in range(n)] for i in range(n, 2 * n)]
    quad4_Y = [[mat_Y[i][j] for j in range(n, 2 * n)] for i in range(n, 2 * n)]

    # Recursively solve for 7 products
    p1 = strassen_mult(quad2_X, subtract_matrices(quad1_Y, quad4_Y))
    p2 = strassen_mult(add_matrices(quad2_X, quad1_X), quad4_Y)
    p3 = strassen_mult(add_matrices(quad3_X, quad4_X), quad2_Y)
    p4 = strassen_mult(quad4_X, subtract_matrices(quad3_Y, quad2_Y))
    p5 = strassen_mult(add_matrices(quad2_X, quad4_X), add_matrices(quad2_Y, quad4_Y))
    p6 = strassen_mult(
        subtract_matrices(quad1_X, quad4_X), add_matrices(quad3_Y, quad4_Y)
    )
    p7 = strassen_mult(
        subtract_matrices(quad2_X, quad3_X), add_matrices(quad2_Y, quad1_Y)
    )

    quad1_Z = add_matrices(p1, p2)
    quad2_Z = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    quad3_Z = add_matrices(p3, p4)
    quad4_Z = subtract_matrices(subtract_matrices(add_matrices(p1, p5), p3), p7)

    mat_Z = [[0 for j in range(2 * n)] for i in range(2 * n)]
    for j in range(n):
        for i in range(n):
            mat_Z[i][j] = quad2_Z[i][j]
            mat_Z[i][j + n] = quad1_Z[i][j]
            mat_Z[i + n][j] = quad3_Z[i][j]
            mat_Z[i + n][j + n] = quad4_Z[i][j]

    return mat_Z


def main():
    result = strassen_mult(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    )
    print(result)


if __name__ == "__main__":
    main()
