for i in range(int(input())):
    stack=[]
    expression=input()
    judge=True
    for j in expression:
        if j=='{' or j=='[' or j=='(':
            stack.append(j)
        else:
            temp=stack.pop(len(stack)-1)
            if (j=='}' and temp=='{') or (j==']' and temp=='[') or (j==')' and temp=='('):
                continue
            else:
                judge=False
                break
    if judge and len(stack)==0:
        print("balanced")
    else:
        print("not balanced")