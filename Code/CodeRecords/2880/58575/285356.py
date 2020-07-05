str=list(map(int,input().split(" ")))
n=str[0]
k=str[1]
a=list(map(int,input().split(" ")))
i=0
while i<a.__len__() and a[i]<=k:
    i=i+1
if i==n:
    print(n)
else:
    j=-1
    while j>-a.__len__() and a[j]<=k:
        j=j-1
    print(i-j-1)