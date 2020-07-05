n=int(input())
flag=True
change=[0 for i in range(n)]
for i in range(n):
    wa,ha=map(int,input().split())
    if(i>0):
        if(ha<=hp):
        elif(wa<=hp):
            change[i]=1
        elif(change[i-1]==1):
            flag=False
        else:
            if(ha<=wp):
                change[i-1]=1
            elif(wa<=wp):
                change[i]=1
                change[i-1]=1
            else:
                flag=False
    wp=wa
    hp=ha
print('YES'if flag else'NO')