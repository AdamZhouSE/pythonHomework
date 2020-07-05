t=int(input())
while t>0:
    t=t-1
    s=input()
    stack=[]
    result=''
    for item in s:
        if (item>='a' and item<='z') or (item>='A' and item<='Z'):
            result=result+item
        else:
            if len(stack)==0:
                stack.append(item)
            else:
                if item=='+' or item=='-':
                    while len(stack)!=0:
                        top=stack[len(stack)-1]
                        if top=='+' or top=='-' or top=='*' or top=='/' or top=='^':
                            result=result+top
                            stack.pop()
                        else:
                            break
                    stack.append(item)
                if item=='*' or item=='/':
                    while len(stack)!=0:
                        top=stack[len(stack)-1]
                        if top=='*' or top=='/' or top=='^':
                            result=result+top
                            stack.pop()
                        else:
                            break
                    stack.append(item)  
                if item=='^':
                    while len(stack)!=0:
                        top=stack[len(stack)-1]
                        if top=='^':
                            result=result+top
                            stack.pop()
                        else:
                            break
                    stack.append(item)
                if item==')':
                    while len(stack)!=0:
                        top=stack[len(stack)-1]
                        if top=='+' or top=='-' or top=='*' or top=='/' or top=='^':
                            result=result+top
                            stack.pop()
                        else:
                            stack.pop()
                            break
                if item=='(':
                    stack.append(item)
    while len(stack)!=0:
        top=stack[len(stack)-1]
        result=result+top
        stack.pop()
    print(result)