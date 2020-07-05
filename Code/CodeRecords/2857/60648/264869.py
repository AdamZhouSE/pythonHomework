n=int(input())
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
m=min(ls)
#print(m)
r=0
for i in range(m):
    count=0
    for j in range(n):
        if ls[j]%(i+1)==0:
            count+=1
    if count==n:
        r+=1
print(r)