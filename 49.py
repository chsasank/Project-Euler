#problem 49:
from numtheory import primesWithin

search = primesWithin(10000)
for i in primesWithin(1000):
    search.remove(i)


def isPermutation(n1,n2):
    temp = n1
    digits = []
    while temp>0:
        digits.append(temp%10)
        temp = temp//10
        
    temp = n2
    while temp>0:
        if temp%10 in digits: digits.remove(temp%10)
        temp = temp//10
        
    if digits: return False
    else: return True
    

for i in search:
    for j in search :
        if j>i and isPermutation(i,j):
            if (i+j)/2 in search:
                if isPermutation((i+j)//2,i):
                    print(i,(i+j)/2,j)
