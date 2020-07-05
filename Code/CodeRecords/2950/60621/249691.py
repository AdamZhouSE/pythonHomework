a=input()
stack=[]
level=0
total=0
for i in a:
    if(i=="2"):
        total+=1
        level+=1
        stack.append(level)
    else:
        total-=1
        if(total<0):
            level=-1
            break
        stack.append(-1*level)
        level-=1
count=0
for i in range(len(stack)):
     count=count+(stack[i])
if count!=0 or level!=0:
    print(-1)
else:
    stack.sort()
    print(stack[len(stack)-1])