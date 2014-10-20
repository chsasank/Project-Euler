#problem 30:
#a bit brute force:
for d6 in range(10):
    for d5 in range(10):
        for d4 in range(10):
            for d3 in range(10):
                for d2 in range(10):
                    for d1 in range(10):
                        if d1**5+d2**5+d3**5+d4**5+d5**5+d6**5 == d1+10*d2+100*d3+1000*d4+10000*d5+100000*d6:
                            print(d6,d5,d4,d3,d2,d1)
