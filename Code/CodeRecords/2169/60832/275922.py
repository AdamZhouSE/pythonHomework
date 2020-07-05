All = int(input())

for q in range(0, All):
    postfix = input()
    stack=[]
    length=len(postfix)

    for c in postfix:
        if c.isdecimal():
            stack.append(int(c))
        else:
            a=stack.pop()
            b=stack.pop()
            if c=='*':
                stack.append(b*a)
            elif c=='/':
                stack.append(b/a)
            elif c=='+':
                stack.append(b+a)
            elif c=='-':
                stack.append(b-a)
    print(stack.pop())
