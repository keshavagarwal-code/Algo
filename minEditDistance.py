def minEditDistance(A, B):
    matrix = [[None for j in range(len(B) + 1)] for i in range(len(A) + 1)]

    for i in range(len(A) + 1):
        matrix[0][i] = i
    
    for i in range(len(B) + 1):
        matrix[i][0] = i

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            min_val = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
            if A[i-1] == B[j-1]:
                matrix[i][j] = min_val
            else:
                matrix[i][j] = min_val + 1
    return matrix[-1][-1]

print(minEditDistance("GRATES", "CREATE"))

    
