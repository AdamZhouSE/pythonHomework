list0=list(input())
a=0
sum=0
isR=False
list1=[]
for i in range(len(list0)):
    if list0[i]=='x':
        if len(list1)==1:
            if isR:
                sum-=int(list1[0])
                list1[0]=0
            else:
                sum+=int(list1[0])
                list1[0]=0
        elif len(list1)==3:
            if (list1[1]=='+' and isR) or (list1[1]=='-' and not isR):
                sum-=int(list1[2])
            else:
                sum+=int(list1[2])
            list1[2]=0
        else:
            if len(list1)==0:
                list1=[0]
                if isR:
                    sum-=1
                else:
                    sum+=1
            else:
                if (list1[1] == '+' and isR) or (list1[1] == '-' and not isR):
                    sum -= 1
                else:
                    sum+=1
                list1.append(0)

    else:
        if list0[i]!='=':
            list1.append(list0[i])
    if len(list1)==3:
        if list1[1]=='+':
            list1=[int(list1[0])+int(list1[2])]
        else:
            list1=[int(list1[0])-int(list1[2])]
    if list0[i]=='=':
        isR=True
        a=list1[0]
        list1=[]
    if i==len(list0)-1:
        a=list1[0]-a

if sum==0 and a==0:
    print('Infinite solutions')
elif sum==0 and a!=0:
    print('No solution')
else:
    x=a//sum
    print('x=',end='')
    print(x)
