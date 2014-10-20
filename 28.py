diag = [1]
squareLength = 3
i = 1

currentOffset = 2
n = 1001
while squareLength < n+1:
    i = i+squareLength-1
    diag = diag + [i]
    
    i = i+squareLength-1
    diag = diag +[i]
    
    i = i+squareLength-1
    diag = diag + [i]
    
    i = i+squareLength-1
    diag = diag + [i]
    
    squareLength = squareLength + 2

print(sum(diag))
#Could have written direct formula, but let it be