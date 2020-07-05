n,x=map(int,input().split())
c=sorted(list(map(int,input().split())))
sum=0
for i in range(n):
    if((x-i)>=1):
        sum+=c[i]*(x-i)
    else:
        sum+=c[i]
print(sum)