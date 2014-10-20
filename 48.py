def modselfpower(n,mod):
    #n**n%mod
    ans = 1
    for i in range(n):
        ans = (ans*n)%mod
        if ans in [0,1]:
            return ans
    return ans

mod = 10**10
print(modselfpower(3,mod))        


sum = 0
for i in range(1, 1001):
    sum = (sum + modselfpower(i,mod))%(mod)

print(sum)
    
