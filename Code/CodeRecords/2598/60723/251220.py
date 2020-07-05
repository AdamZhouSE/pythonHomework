temp=input().split()
M=int(temp[0])
D=int(temp[1])
t=0
list=[]
for i in range(M):
    temp=input().split()
    if temp[0]=='Q':
        L=int(temp[1])
        result=max(list[len(list)-L:])
        t=result
        print(result)
    else:
        if len(temp)==2:
            n=int(temp[1])
        else:
            n=int(temp[0][1:])
        result=(n+t)%D
        list.append(result)