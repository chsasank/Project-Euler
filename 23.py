from nummath import sumDivisors

def sumProperDivisors(i): return sumDivisors(i) - i

abundantNumbers = []
for i in range(1,29000):   
    if sumProperDivisors(i) > i:
        abundantNumbers.append(i)


n = 29001
isSumAbundant = [False for x in range(0,n)]

for i in range(len(abundantNumbers)):
    for j in range(i, len(abundantNumbers) ):
        sumAbundant = abundantNumbers[i] + abundantNumbers[j]
        if sumAbundant<n:
            isSumAbundant[sumAbundant] = True
        

ans = 0
for i in range(len(isSumAbundant)):
    if isSumAbundant[i] == False:
        ans = ans+i

print(ans)