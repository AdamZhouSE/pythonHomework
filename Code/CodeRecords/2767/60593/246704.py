t=int(input())
for tt in range(t):
    n=int(input())
    ans=0
    for i in range(0,n//3+1):
        for j in range(0,n//5+1):
            for k in range(0,n//10+1):
                if(i*3+j*5+k*10==n):
                    ans+=1
    print(ans)
