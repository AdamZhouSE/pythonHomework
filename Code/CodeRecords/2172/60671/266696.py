def priority(z):
    if z in ['×', '*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1
    elif z in ['^']:
        return 3
    
time=int(input())
while(time>0):
    time-=1
    instr=input()
    
    stack=[]
    poststr=""
    
    for z in instr:
        if z not in ['×', '*', '/', '+', '-', '(', ')','^']:
            poststr+=z
        else:
            if (z != ')') and (not stack or z == '(' or stack[-1] == '('or priority(z) > priority(stack[-1])): 
                stack.append(z)
            elif z == ')': 
                while True:
                    x = stack.pop()
                    if x != '(':
                        poststr+=x
                    else:
                        break

            else: 
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        poststr+=stack.pop()
                    else:
                        stack.append(z)
                        break
    while stack:
        poststr+=stack.pop()
    print(poststr)
