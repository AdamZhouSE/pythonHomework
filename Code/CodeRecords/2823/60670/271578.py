n,k=map(int,input().split())
list[0 for i in range(0,n+1)]
for i in range(2,n+1):
    tmp=1
    while tmp<=n:
        tmp*=i
        if tmp<=n:
            list[i]+=1
print(list)