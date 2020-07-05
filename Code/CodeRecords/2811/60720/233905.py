line1=input().split()
p=int(line1[0])
x=int(line1[1])
list=[-1]*300
ifend=0
for i in range(x):
    if(ifend==1):
        break
    else:
        number=int(input())
        if(list[number%p]==-1):
            list[number%p]=number
        else:
            print(i+1)
            ifend=1
if(ifend==0):
    print(-1)