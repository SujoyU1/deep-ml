def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    row=len(a)
    column=len(a[0])

    result=[[0 for i in range(row)] for j in range(column)]

    for i in range(row):
        for j in range(column):
            result[j][i]=a[i][j]
    return result

    