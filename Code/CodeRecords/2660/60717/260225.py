n=int(input())
stack=[]
for i in range(0,n):
    tmp=input().split()
    if tmp[0]=='T':
        stack.append(tmp[1])
    elif tmp[0]=='U':
        count=int(tmp[1])
        for i in range(0,count):
            stack.pop()
    else:
        print(stack[int(tmp[1])-1])