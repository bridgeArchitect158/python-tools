# import library
import numpy as np

# solving a system of linear equations
A = np.array([[3, 2],
              [4, 5]])
b = np.array([7, 23])
solution = np.linalg.solve(A, b)
print("Solution (x, y):", solution)

# finding eigenvalues of a matrix
matrix = np.array([[1, 2],
                   [3, 4]])
eigenvalues = np.linalg.eigvals(matrix)
print("Eigenvalues:", eigenvalues)

# calculating the inverse of a matrix
det = np.linalg.det(matrix)
# check determinant to ensure the matrix is invertible
if det != 0:
    invMatrix = np.linalg.inv(matrix)
    print("Inverse of the matrix:\n", invMatrix)
else:
    print("The matrix is singular and not invertible.")
