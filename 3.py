from math import sqrt

num  = 600851475143
# to find largest prime factor


# wrong Algo!
### Algo 1: factorise from upside rather than from 0
##i = int(sqrt(num)) #this sqrt thing is wrong as well! this will not give us largest factor!
##while i > 0:
##    if i == 1:
##        break
##    if num%i == 0: # if i is the largest factor of num, now factorise i.
##        num = i
##        print(num)
##        i = int(sqrt(num))
##        continue
##    i = i -1


num = int(input('which number do you want to factorise? '))

#below is factorisation algo, without finding prime numbers!

#correct algo, yeah!!!
#let's start from bottom, find first factor,
#remove it and find first factor of this num and so on.
#basically, we're removing small prime factors, aka factorising?
i = 2
while i <= int(sqrt(num)):
    if num%i == 0:
        print( num, '=' , i, '*', num//i )
        num = num//i
        i = 2
        continue
    i = i + 1
