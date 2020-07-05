a=[int(x) for x in input().split(",")]
a.sort()
count=0
same=0
now=-1
while len(a)>0:
    i=a.pop(0)
    count+=1
    if now==i and same>0:
        same-=1
    else:
        if same>0:
            count+=same
        same=i
    now=i
count+=same
print(count)