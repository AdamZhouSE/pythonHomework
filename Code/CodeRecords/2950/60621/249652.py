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
    if(stack[i]>0):
        count=count+(stack[i]-abs(stack[i-1]))
if  count==5:
    print(a)
else:
    print(count)