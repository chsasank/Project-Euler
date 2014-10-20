from nummath import sumDivisors

def sumProperDivisors(i): return sumDivisors(i) - i


amicableNumbers = []
for i in range(3,10000):
    di = sumProperDivisors(i)
    if(i != di):
        if (i == (sumProperDivisors(di))):
            amicableNumbers = amicableNumbers + [i]

print(sum(amicableNumbers))
