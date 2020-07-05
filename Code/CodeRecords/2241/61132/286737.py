n=int(input())
sum=0
for l in range(1,n+1):
    tmp=n/l-(l-1)/2
    if tmp==int(tmp) and tmp>0 and tmp+l-1<=n:
        sum+=1
print(sum)