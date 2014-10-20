from numtheory import factorial

#print(factorial(10))


#for problem 24,(uncomment the following:)
#need millionth lexicogarphic permuation
n = 10
num = int(input('which permuatation?'))
unused = [x for x in range(0,n)]
rev = [x for x in range(n-1,-1, -1)]
print(rev)
for i in rev:
    a = num//factorial(i)
    print(unused.pop(a), end = '')
    num = num%factorial(i)
    
