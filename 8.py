num = input("give the number: ")
max = 0
i = 4
while i < len(num):
    prod = int(num[i])*int(num[i-1])*int(num[i-2])*int(num[i-3])*int(num[i-4])
    if prod > max:
        max = prod
    i = i+1

print(max)
