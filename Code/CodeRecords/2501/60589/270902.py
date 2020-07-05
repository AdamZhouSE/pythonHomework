n=int(input())
old=input().split(' ')
new=input().split(' ')
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        a=old[i]
        b=old[j]
        if new.index(a)>new.index(b):
            ans+=1
print(ans)