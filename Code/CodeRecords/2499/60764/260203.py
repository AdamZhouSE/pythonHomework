n=int(input())
stack=[]
for i in range(n):
    command=input().split()
    if command[0]=='Add':
        stack.append(command)
    elif command[0]=='Del':
        ind=int(command[1])
        if ind-1>=0 and ind-1<len(stack):
            stack[ind-1][0]='No'
    else:
        x=int(command[1])
        res=0
        for j in range(len(stack)):
            if stack[j][0]=="Add":
                tem=int(stack[j][1])*x+int(stack[j][2])
                if tem>int(stack[j][3]):
                    res+=1
        print(res)