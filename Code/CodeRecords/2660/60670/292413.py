n=int(input())
stack=[]
for i in range(0,n):
    op=input().split()
    if op[0]=='T':
        stack.append(op[1])
    elif op[0]=='U':
        for j in range(0,int(op[1])):
            stack.pop()
    else:
        print(stack[int(op[1])-1])