coins = [1,2,5,10,20,50,100,200]

n = int(input())+1
m = len(coins)

#C[i][j] is number of ways to make $i with 0:j coins
C = [[0 for x in range(m)] for x in range(n)]

#C[i][0] is 1 because only one coin is avaiable
for i in range(n):
    C[i][0] = 1

#C[0][i] is 1 because there is only one way to make $0: use no coin
for j in range(m):
    C[0][j] = 1

#dp eqn
for i in range(1,n):
    for j in range(1,m):
    	if i - coins[j] >= 0:
    		C[i][j] = C[i][j-1] + C[i-coins[j]][j]
    	else:
    		C[i][j] = C[i][j-1]

#print answer
print(C[n-1][m-1])
