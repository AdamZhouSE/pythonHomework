a=input()
sign=a[0]
stack=[]
i=0;flag=True
while sign!="@":
    i+=1

    if(sign=="("):
        stack.append(sign)
    elif(sign==")"):
        if len(stack)==0:
            print("NO",end="")
            flag=False
            break
        else:
            stack.pop()
    sign = a[i]
if(flag):
    if(len(stack)==0):
        print("YES",end="")
    else:
        print("NO",end="")
