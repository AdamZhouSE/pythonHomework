n= int(input())
a=[]*n
b=[]*n
for i in range(0,n):
    a[i],b[i]=map(int,input().split())
re=0
for i in range(0,n):
    for j in range(0,n):
        if a[i]>a[j] and b[i]<b[j]:
            re=1
if re==0:
    print("Poor Alex")
else:
    print("Happy Alex")
            