a=input()
sign=a[0]
stack=[]
i=0;flag=True
while sign!="@":
    i+=1
    sign=a[i]
    if(sign=="("):
        stack.append(sign)
    elif(sign==")"):
        if len(stack)==0:
            print("NO")
            flag=False
            break
        else:
            stack.pop()
if(flag):
    print("YES")
