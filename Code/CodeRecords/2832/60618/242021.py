n=int(input())
a=[int(n) for n in input().split()]
a.insert(0,0)
day=0
for i in range(1,n+1):
    if a[i]==i:
        day+=1
print(day-1)
        