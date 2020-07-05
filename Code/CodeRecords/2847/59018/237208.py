n=int(input())
info1=input().split(' ')
a=[int(y) for y in info1]
info2=input().split(' ')
b=[int(y) for y in info2]
if b[1]<=b[0]:
    print(0)
else:
    count=0
    for i in range(b[0]-1,b[1]-1):
        count=count+a[i]
    print(count)   
        