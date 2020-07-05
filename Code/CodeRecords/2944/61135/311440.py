inp=input()
inp=list(inp)
stack=[]
result=True
for i in range(len(inp)):
    if inp[i] == "(":
        stack.append("(")
        continue
    elif inp[i]==")":
        if len(stack)!=0:
            stack.pop()
            continue
        else:
            result=False
            break
    else:
        continue
if(len(stack)==0 and result):
    print("YES",end="")
else:
    print("NO",end="")