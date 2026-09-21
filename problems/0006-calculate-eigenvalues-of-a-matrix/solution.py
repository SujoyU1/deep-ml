def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace=matrix[0][0]+matrix[1][1]
	determinant=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	eigenvalues=[]
	eigenvalues.append((trace+(trace**2-4*determinant)**0.5)/2)
	eigenvalues.append((trace-(trace**2-4*determinant)**0.5)/2)

	return eigenvalues