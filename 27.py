from nummath import isPrime,primesWithin

brange = primesWithin(1000)

nmax = 0
amax = 0
bmax = 0
for b in primesWithin(1000):
    for a in range(-1000,1001):
        n = 0
        while(isPrime(n**2 + a*n + b)): 
            n = n+1
    
        if n>nmax:
            amax = a
            bmax = b
            nmax = n

print(amax*bmax)
        