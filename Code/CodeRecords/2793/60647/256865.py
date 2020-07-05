a=input().split()
c=int(a[1])
list=input().split()
num=0
for i in range(len(list)-1):
    if int(list[i+1])-int(list[i])<=c:
        if num==0:
            num=2
        else:
            num+=1
    else:
        num=0
if len(list)==1:
    num=1
print(num)