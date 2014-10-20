from nummath import factorize

def power(factorization,i):
    """
    Assumes l contains factorization of a number
    Returns factorization of l**i
    """
    ans = []
    for l in factorization:
        ans.append([l[0],l[1]*i])
    
    return ans


distinctPowers = []

for i in range(2,101):
    factorization = factorize(i)
    for j in range(2,101):
        lj = power(factorization,j)
        if lj not in distinctPowers:
            distinctPowers.append(lj)


print(len(distinctPowers))

# l = factorize(24)
# print(power(l,4), "  ", l)