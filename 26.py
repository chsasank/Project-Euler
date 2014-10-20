from numtheory import primesWithin
#Problem 26:
primeList = primesWithin(1000)
primeList.remove(2)
primeList.remove(3)
primeList.remove(5)
#remve all primes that appeared as factor in 10^m -1 until 1 remained
m = 2
while len(primeList)!=1:
    #print(primeList)
    num = (10**m-1)//9
    dup = primeList
    for prime in primeList:
        if num%prime==0:
            dup.remove(prime)

    primeList = dup
    m = m+1

print(primeList)
