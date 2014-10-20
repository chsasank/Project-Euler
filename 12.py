from numtheory import divisors
#Problem 12
n = 5
while n!=0:
    #here I am using the fact that n//2 and n+1 are coprimes! Otherwise not true!
    if n%2 == 0:
        numDiv = divisors(n//2)*divisors(n+1)
    else:
        numDiv = divisors((n+1)//2)*divisors(n)

    if numDiv >= 500:
        break

    n = n+1

print(n*(n+1)//2)
