def add_integer(a, b=98):
    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("B must be an integer")
    
    a = int(a)
    b = int(b)

    return a+b



def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix)):
         raise TypeError("matrix must be matrix (list of lists) of integeres/floats")
    
    row_length = len(matrix[0]) if matrix else 0
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    

    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row :
            new_row.append(round(num/div, 2))
        new_matrix.append(new_row)

    return new_matrix
         
   
    
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    

def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 :
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    # method 1
    for _ in range(size):          
        for _ in range(size):      
            print("#", end="")     
        print()
    # method 2
    for i in range(size):
        print("#" *size)
      

print_square(4)