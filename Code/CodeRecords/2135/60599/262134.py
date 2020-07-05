s=list(map(int,input().split(',')))
minS=max(s)*len(s)
for i in range(min(s),max(s)+1):
    sum=0
    for k in s:
        sum+=abs(i-k)
    minS=min(minS,sum)
print(minS)