from numtheory import factorize
#Problem 47:
n = 5
#2,3,4
distinctPrimesFactors = [1,1,1]
while n != 0:
    distinctPrimesFactors.append(len(factorize(n)))
    if distinctPrimesFactors[-1] == 4:
        if distinctPrimesFactors[-2] == 4:
            if distinctPrimesFactors[-3] ==4:
                if distinctPrimesFactors[-4] == 4:
                    break

    n = n+1
print(n)

