n=int(input())
for i in range(0,n):
    x=int(input())
    move=input().split()
    list1=[0,0,0,0]
    index=0
    dirc=0
    while index<len(move):
        a=move[index]
        b=int(move[index+1])
        index+=2
        if a=='U':
            list1[dirc]+=b
        elif a=='R':
            dirc+=1
            if dirc==4:
                dirc=0
            list1[dirc]+=b
        elif a=='D':
            dirc+=2
            if dirc>=4:
                dirc-=4
            list1[dirc]+=b
        else:
            dirc-=1
            if dirc==-1:
                dirc=3
            list1[dirc]+=b
    dis=int(((list1[0]-list1[2])**2+(list1[1]-list1[3])**2)**0.5)
    strr=str(dis)+' '
    if dirc==0:
        strr+='N'
    elif dirc==1:
        strr+='E'
    elif dirc==2:
        strr+='S'
    else:
        strr+='W'
    print(strr)