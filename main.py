import Numpy as np
# Để cộng 2 ma trận
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B
print(C)
# Để nhân 2 ma trận
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = np.dot(A, B)
print(C)

# Với phép nhân Vecto nhiều chiều thì ta sử dụng toán tử "*"
C = A * B
# Để chuyển vị 1 ma trận
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose())
# Để tính toán ma trận đảo ngược
a = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
ainv = np.inv(a)
# Để tính toán hạng của ma trận
linalg.matrix_rank(A, tol=None, hermitian=False)

# Để tính định thức của ma trận
a = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
print(np.linalg.det(a))
