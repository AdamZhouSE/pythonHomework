n=int(input())
temp=[int(x) for x in input().split(' ')]
step=0
for i in range(n):
    if(temp[i]<0):
        step+=(-1-temp[i])
        temp[i]=-1
    elif(temp[i]>0):
        step+=temp[i]-1
        temp[i]=1
mul=1
for x in temp:
    if(x!=0):
        mul*=x
for x in temp:
    if(x==0):
        if(mul==-1):
            step+=1
            mul=1
        else:
            step+=1
if(mul==-1):
    print(step+2)
else:
    print(step)