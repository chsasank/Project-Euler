n = int(input('size?')) + 1

matrix = [ [0 for x in range(n)] for x in range(n)]

#edge conditions
for e in range(0,n):
    matrix[e][0] = 1
    matrix[0][e] = 1
    

for i in range(1,n):
    for j in range(1,n):
        matrix[i][j] = matrix[i][j-1] + matrix[i-1][j] 


print(matrix[n-1][n-1])
