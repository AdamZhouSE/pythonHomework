n,x=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
c.sort()
sum=0
for i in c:
    sum= sum+(i*x)
    x = x-1 
    if x <= 0:
        x = 1
print(sum)