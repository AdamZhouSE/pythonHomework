n,t=map(int,input().split())
a=list(map(int,input().split()))
max1=0
for i in range(n):
    tmptime=0
    tmpbook=0
    for j in range(i,n):
        tmptime+=a[j]
        if tmptime<=t:
            tmpbook+=1
    max1=max(max1,tmpbook)
print(max1)