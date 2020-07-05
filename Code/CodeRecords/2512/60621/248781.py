a=[int(x) for x in input().split()]
num=a[0];p=a[1]
b=[int(x) for x in input().split()]
c=input()
for i in range(int(c)):
    temp=[int(x) for x in input().split()]
    operation=temp[0]
    start,end=temp[1]-1,temp[2]

    if(operation==1):
        co = temp[3]
        for j in range(start,end):
            b[j]=b[j]*co
    elif(operation==2):
        co = temp[3]
        for j in range(start,end):
            b[j]=b[j]+co
    else:
        to=0
        for j in range(start,end):
            to+=b[j]
        print(to%p)
