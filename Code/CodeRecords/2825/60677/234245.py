people=int(input())
sort=list(range(people))
for i in range(people):
    x=input().split()
    sum=0
    for j in x:
        sum+=int(j)
    sort[i]=sum
smith=sort[0]
sort.reverse()
print(sort.index(smith)+1)