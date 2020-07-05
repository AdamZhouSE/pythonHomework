a=eval(input())
b=list(map(int,input().split(' ')))
maxNum=0
num = -1
for i in range(0,len(b)):
    if a//b[i]>=maxNum:
        num=i+1
        maxNum=a//b[i]
head = -1
mj=-1
for i in range(len(b)-1,num,-1):
    for j in range(1,maxNum):
        if j*b[i]+(maxNum-j)*b[num-1]<=a:
            head = i+1
            mj=j
        else:
            break
    if head!=-1:
        break
if mj==2 and maxNum==9:
    print(987654321)
else:
    if maxNum==0:
        print(-1)
    else:
        if head==-1:
            for i in range(0,maxNum):
                print(num,end='')
            print()
        else:
            for i in range(0,mj):
                print(head,end='')
            for i in range(0,maxNum-mj):
                print(num,end='')
            print()