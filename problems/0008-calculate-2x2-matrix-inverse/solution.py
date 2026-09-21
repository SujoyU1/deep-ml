def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    if matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]==0:
        return None
    else:
        invsere_step1=[[matrix[1][1],-matrix[0][1]],[-matrix[1][0],matrix[0][0]]]
        determinant=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        for i in range(len(invsere_step1)):
            for j in range(len(invsere_step1[0])):
                invsere_step1[i][j]=invsere_step1[i][j]/determinant
        inverse=invsere_step1
    return inverse

    