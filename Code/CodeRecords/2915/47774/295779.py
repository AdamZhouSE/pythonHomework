n=int(input())
ss=input()
a=[int(i) for i in ss.split(' ')]
ans=0
for i in range(n):
    j=i
    while j+1<n and a[j+1]<=a[j]*2:
        j+=1
    ans = max(ans,j-i+1)
    i=j
print(ans)
