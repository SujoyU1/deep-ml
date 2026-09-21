def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
  means=[]
  
  if mode=='row':
    for i in range(len(matrix)):
      rowlist=0
      for j in range(len(matrix[0])):
        rowlist+=matrix[i][j]
      means.append(rowlist/len(matrix[0]))

  else:
    for i in range(len(matrix[0])):
      columnlist=0
      for j in range(len(matrix)):
        columnlist+=matrix[j][i]
      means.append(columnlist/len(matrix))
                  
                   

      

  return means