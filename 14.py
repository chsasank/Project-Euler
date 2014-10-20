def collatz(n):
    if n==1: return [1]
    
    if n%2 == 0: return [n] + collatz(n//2)
    else: return [n]+ collatz(3*n+1)
    


collatzLength = dict()
n = 1000000
maxLength = -1
maxIndex = 0
collatzLength[1] = 1
for i in range(2,n):
    
    num = i
    tempLength = 0
    while num !=1:
        if num%2 == 0 :
            num = num//2
        else:
            num = 3*num+1
    
        tempLength = tempLength + 1
        
        if num in collatzLength:
            collatzLength[i] = tempLength + collatzLength[num]
            break
            
    if(collatzLength[i]>maxLength):
        maxLength = collatzLength[i]
        maxIndex = i

    num = i
    tempLength = 0
    while num !=1:
        if num%2 == 0 :
            num = num//2
        else:
            num = 3*num+1
    
        tempLength = tempLength + 1
        
        if num in collatzLength:
            break
        
        collatzLength[num] = collatzLength[i] - tempLength

print(maxIndex)
#
# for i in range(1,n):
#     print(collatz(i), " len =  ", collatzLength[i] )
