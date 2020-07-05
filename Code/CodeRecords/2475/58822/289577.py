num=int(input())
for i in range(num):
    j=int(input())
    n=input().split(' ')
    n=list(map(int,n))
    n=sorted(n,reverse=False)
    times=0
    max=0
    for i in range(j):
        times=1
        for k in range(i+1,j):
            if(n[k]==(n[k-1]+1)):
                times+=1
            else:
                if(max<times):
                    max=times
                    break
    print(max)