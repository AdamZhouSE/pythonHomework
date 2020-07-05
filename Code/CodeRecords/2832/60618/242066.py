n=int(input())
a=[int(n) for n in input().split()]
a.insert(0,0)
day=0
for i in range(1,n+1):
    if a[i]==i:
        day+=1
        for j in range(1,i+1):
            if a[j]>i:
                i=i+1
                day=day-1
                break
        
print(day)
        