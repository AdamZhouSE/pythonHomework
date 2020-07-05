s=input()
stack=[]
check=True
top=0
for i in range(len(s)):
    if s[i]=='2':
        stack.insert(0,s[i])
        if len(stack)>top:
            top=len(stack)
    elif s[i]=='5':
        if len(stack)>0:
            stack.pop(0)
        else:
            check=False
            break
if len(stack)!=0 or check==False:
    print(-1)
else:
    print(top)