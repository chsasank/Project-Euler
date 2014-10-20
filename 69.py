from numtheory import primesWithin

primes = primesWithin(100)
mult = 1
for i in primes:
    mult1 = mult*i
    if mult1>1000000:
        print(mult)
        break
    mult= mult1
