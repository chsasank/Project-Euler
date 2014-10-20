from itertools import permutations
from nummath import isPrime,number


for i in list(permutations([7,6,5,4,3,2,1])):
    if isPrime(number(i)) == True: 
        print(number(i))
        break