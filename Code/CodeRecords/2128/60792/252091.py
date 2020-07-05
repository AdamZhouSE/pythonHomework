list1=list(map(int,input().split(",")))
f=0
for i in range(0,len(list1)+1):
    temp=0
    for j in range(0,len(list1)):
        temp=temp+list1[(j+i)%len(list1)]*j
    if temp>f:
        f=temp
print(f)