import numpy as np

def square_matrix(matrix):
    """
    This function takes a 2D matrix and returns its square.
    It uses NumPy to perform element-wise squaring.
    
    Example usage:
    >>> matrix = [[1, 2], [3, 4]]
    >>> result = square_matrix(matrix)
    >>> print(result)
    [[1, 4], [9, 16]]

    :param matrix: A 2D NumPy array
    """
    return np.square(matrix)

# Example usage:
matrix = np.array([[5, -3], [4, 7]])
result = square_matrix(matrix)
print(result)
