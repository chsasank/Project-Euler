def fib(n):
    #returns fib sequence until n
    a = 0
    b = 1
    sum = 0
    while b <= n:
        a,b = b, a+b
        if a%2 == 0:
            sum = sum + a

    return sum

print(fib(4000000))
