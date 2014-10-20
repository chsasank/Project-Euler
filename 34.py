from numtheory import factorial
fact = [factorial(i) for i in range(10)]
print(fact)
for i in range(10, 7*fact[9]):
    possible = True
    temp = i
    s = 0
    while temp>0:
        s = s+ fact[temp%10]
        if s > i:
            possible = False
            break
        temp = temp//10
    
    if possible == False: continue

    if i == s: print(i)
