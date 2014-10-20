for a in range(1,10):
    for b in range(1,10):
        for c in range(a+1,10):
            if (10*a+b)/(10*b+c) == a/c:
                print(10*a + b, 10*b + c)
