s=input()
stack=[]
res="YES"
for i in range(len(s)):
    if s[i]=='(':
        stack.insert(0,s[i])
    elif s[i]==')':
        if len(stack)==0:
            res="NO"
            break
        else:
            stack.pop(0)
if len(stack)!=0:
    print("NO",end="")
else:
    print(res,end="")