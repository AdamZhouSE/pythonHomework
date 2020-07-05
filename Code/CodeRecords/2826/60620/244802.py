n=int(input())
a=sorted(list(map(int,input().split())))
s=sum(a)
for i in range(n-1):
    if(a[i]>=a[i+1]):
        a[i+1]=a[i]+1     
print(sum(a)-s)
