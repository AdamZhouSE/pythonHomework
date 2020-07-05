nk = list(map(int,input().split()))
l = [[0]*(nk[1]+1) for i in range(nk[0]+1)]
if nk[1]==1:
    print(nk[0])
else:
    for i in range(1,nk[0]+1):
        l [i][1]=1
        for j in range(i,nk[0]+1,i):
            for v in range(2,nk[1]+1):
                l[j][v]+=l[i][v-1]
    sum1=0 
    for i in range(nk[0]+1):
        sum1 +=l[i][nk[1]]
    print(sum1)
          