from nummath import digits
file = open('data.txt','r')

sum = 0
for i in range(100):
    sum = sum + int(file.readline())
    
d = digits(sum)
print(d[:10])