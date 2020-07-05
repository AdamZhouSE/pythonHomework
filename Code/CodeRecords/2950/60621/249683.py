a=input()
stack=[0]
level=0
for i in a:
    if(i=="2"):
        level+=1
        stack.append(level)
    else:
        stack.append(-1*level)
        level-=1
count=0
for i in range(1,len(stack)):
     count=count+(stack[i])
if count!=0 or level!=0:
    print(-1)
else:
    stack.sort()
    print(stack[len(stack)-1])