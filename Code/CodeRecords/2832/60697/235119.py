num=int(input())+1
sizes=list(map(int,input().split(' ')))
sizes.insert(0,0)
i=1
res=0
while i<num:
    maxsize=sizes[i]
    while i<=maxsize:
        maxsize=max(sizes[i],maxsize)
        i=i+1
    res=res+1
print(res)