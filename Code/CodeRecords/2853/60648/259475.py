n=int(input())
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
c=0
for i in range(n):
    r=0
    for j in range(n):
        r+=ls[j]
    r-=ls[i]
    if r%2==0:
        c+=1
print(c)