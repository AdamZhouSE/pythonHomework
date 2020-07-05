n=int(input())
res,d=0,0
stack=list()
for i in range(n,0,-1):
    if stack:
        if d%4==0:
            val=stack.pop()
            stack.append(val*i)
        elif d%4==1:
            val=stack.pop()
            stack.append(val//i)
        elif d%4==2:
            stack.append(i)
        elif d%4==3:
            stack.append(-i)
        d+=1
    else:
        stack.append(i)
if stack:
    for i in stack:
        res+=val
print(res)