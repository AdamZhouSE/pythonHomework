n=int(input())
a=[]
for i in range(n):
    info=input().split(',')
    for y in info:
        a.append(int(y))
k=int(input())
a.sort()

first=0
last=len(a)
while first<last:
    mid=(first+last)//2
    if mid<8:
        first=mid+1
    elif mid>8:
        last=mid-1
    else:
        break
print(a[mid])
         
