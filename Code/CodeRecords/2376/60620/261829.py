n=int(input())
tar=[0 for i in range(n+1)]
tar[1]=0
if(n<=1):
    print(0)
else:
    tar[2]=1
    for i in range(3,n+1):
        for j in range(1,i//2):
            if(i%j==0 and tar[i-j]==0):
                tar[i]=1
                break
    if(tar[n]==1):
        print(True)
    else:
        print(False)