people=int(input())
p=list(range(people))
for i in range(people):
    x=input().split()
    sum=0
    for j in x:
        sum+=int(j)
    p[i]=sum
smith=p[0]
p.sort(reverse=True)
y=p.index(smith)
print(y+1)