#we have 23c10>10^6, so for n>23, we only need to search n cr, for r<10. 
total = 0
candidates = dict()
l = []
for n in range(1,301):
    ans = n
    for i in range(2,1+ n//2):
        ans = ans*(n-i+1)//(i)
        #this ans is same as (n c i)
        #if ans > 1000000:

        #checking for non trivial repetitions
        if ans in candidates:
            temp = '='+str(n) + 'C' + str(i)
            candidates[ans].append(temp)
            
        else: candidates[ans] = ['='+str(n)+ 'C'+str(i)]

            
            
        

l = [ [i,candidates[i]] for i in candidates if len(candidates[i]) > 1]
print(l)
