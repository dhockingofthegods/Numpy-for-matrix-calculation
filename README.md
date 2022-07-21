# Numpy for Matrix
### Numpy là một thư viện dùng để xử lý dạng dữ liệu mảng trong Python tuy rằng trong Python cũng có "List" một dạng dữ liệu dùng để làm việc với mảng, tuy nhiên việc sử dụng Numpy cho phép xử lý dữ liệu nhanh hơn 50x.
### Numpy là một trong những thư viện phổ biến trong Python dành cho việc tính toán ma trận, trong Numpy có một thư viện hay dùng để tính toán ma trận đó là numpy.linalg
## Để cộng 2 ma trận
    A = np.array([[2, 4], [5, -6]])
    B = np.array([[9, -3], [3, 6]])
    C = A + B  
    print(C)
## Để nhân 2 ma trận
    A = np.array([[2, 4], [5, -6]])
    B = np.array([[9, -3], [3, 6]])
    C = np.dot(A,B)  
    print(C) 
### Với hàm dot() Nếu Vecto có dạng 1-D thì hàm sẽ trả về tích bên trong của các Vecto với Vecto có dạng 2-D thì hàm này tương tự như phép nhân Vecto thông thường, còn với dạng N-D thì nó là một tích tổng trên trục cuối cùng của a và trục cuối cùng thứ hai của b.
### Với phép nhân Vecto nhiều chiều thì ta sử dụng toán tử "*"
    C = A*B
## Để chuyển vị 1 ma trận
    A = np.array([[1, 1], [2, 1], [3, -3]])
    print(A.transpose())
## Để tính toán ma trận đảo ngược
    a = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
    ainv = np.inv(a)
## Để tính toán hạng của ma trận
    linalg.matrix_rank(A, tol=None, hermitian=False)
### Trong đó A có thế mà mà trận hoặc là stack of matrix, hàm tính toán ma trận bằng cách sử dụng công thức SVD và trả về hạng của ma trận
## Để tính định thức của ma trận
    a = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
    print(np.linalg.det(a))
    
