n,k=list(map(int,input().strip().split()))
a=list(map(int,input().strip().split()))
b=[0]*n
for i in range(n-1):
    b.append(a[i]-a[i+1])
b.sort()
print(sum(b[:k-1])+max(a)-min(a))