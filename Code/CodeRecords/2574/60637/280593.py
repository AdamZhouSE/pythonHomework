tests=(int)(input())
prim=[2]
for i in range(tests):
    n=(int)(input())
    j=prim[-1]+1
    while(len(prim)<n):
       judge=True
       for k in range(2,j):
            if(j%k==0):
                judge=False
                break
       if(judge):
            prim.append(j)
       j+=1
    print(pow(prim[n-1],2)+1)