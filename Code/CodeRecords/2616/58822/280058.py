def isD(a,b):
    if a==1:
        if b==1:
            return 1
        else:
            return 0
    if(b==2 and a!=1):
        return 1
    sum=0
    for i in range(1,b+1):
        sum=sum+i
    if(sum<=a):
        return 1
    else:
        return 0
num=int(input())
li=[]
for i in range(num):
    li.append(input())
n=[]
res=[]
for i in range(num):
    print(isD(int(li[i][0]),int(li[i][2])))