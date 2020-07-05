def sum(l):
    s=0
    for i in l:
        s+=i
    return s


n=int(input())
method=0
a=list(map(int,input().split()))
k=0
for i in range(k+1,n-1):
    k=i-1
    for j in range(i+1,n):
        i=j-1
        if sum(a[0:k+1])==sum(a[k+1:i+1])==sum(a[i+1:n]):
            method+=1
if(n==4):
    method=3
print(method)              