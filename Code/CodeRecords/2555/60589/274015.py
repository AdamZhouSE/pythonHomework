n=int(input())
a=input().split(' ')
a=list(map(int,a))
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]<a[j]<a[k]:
                ans+=1
print(ans,end='')