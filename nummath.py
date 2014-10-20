#Library containing some number theory functions.
from math import sqrt, log

def factorial(n):
    """
    Returns n!
    """
    ans = 1;
    for i in range(1,n+1):
        ans = ans*i 
        
    return ans

def gcd(a,b):
    """
    Returns greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def digits(n):
    """
    Returns list containing digits of n
    """
    d = []
    i = n
    while i != 0:
        d.append(i%10)
        i = i//10
    
    d.reverse()
    return d

def number(digits):
    """
    Gives number corresponding to digits
    """
    num = 0;
    for i in range(len(digits)):
        num = num + (10**i)*digits[- i-1]
        
    return num
        
def factorize(num):
    """
    Factorisation algorithm without finding prime numbers!
    
    let's start from bottom, find first factor,
    remove it and find first factor of this num and so on.
    basically, we're removing small prime factors, aka factorising

    output will be nest list. first element of element is prime.
    Second is its power
    """
    factorization = [[1,1]]
    i = 2
    while i <= int(sqrt(num)):
        if num%i == 0:
            if i != factorization[-1][0]:
                factorization.append([i,1])
            else:
                factorization[-1][1] = factorization[-1][1]+1
            num = num//i
            i = 2
            continue
        i = i + 1

        
    if num != factorization[-1][0]:
        factorization.append([num,1])
    else:
        factorization[-1][1] = factorization[-1][1]+1
    factorization.remove([1,1])
    return factorization

def divisors(num):
    """
    Returns number of divisor of a num
    """
    factorization = factorize(num)
    numDiv = 1
    for l in factorization:
        numDiv = numDiv*(1+l[1])

    return numDiv

def sumDivisors(num):
    """
    Returns sum of all divisors of num
    """
    if num == 1:
        return 1
        
    factorization = factorize(num)
    sumDiv = 1
    for l in factorization:
        p = l[0]
        sumDiv = (p**(1+l[1])-1)//(p-1)*sumDiv

    return sumDiv

def primesWithin(n):
    """
    Sieve of erosthanes
    """
    #using dict as list is too slow
    primes = dict()
    for i in range(2,n): primes[i] = True

    for i in primes:
        factors = range(i, n, i) #nice way to iterate over factors!
        for f in factors[1:i]:
            primes[f] = False

    return [ i for i in primes if primes[i] == True]
    
def nthPrime(n):
    """
    Returns nth prime prime number
    """
    #will use prime number theorem result, found in wikipedia and stack exchange:
    #p_n< n*ln(n)+n(ln(ln(n)) for n≥6
    #then seive this range.
    h = int(n*log(n)+n*( log(log(n))))
    primes = primesWithin(h)  
    return primes[n-1]
    
def isPrime(n):
    """
    Returns true if n is a prime
    """
    if n <= 0 : return False 
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
            
    return True