def priority(z):
    if z in '^':
        return 3
    elif z in ['×', '*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1
def in2post(expr):
    stack = []
    post = []
    for z in expr:
        if z not in ['×', '*', '/', '+', '-', '(', ')','^']: 
            post.append(z)

        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('
                             or priority(z) > priority(stack[-1])):  
                stack.append(z)     

            elif z == ')':  
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
                    else:
                        break
            else:  
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        post.append(stack.pop())
                    else:
                        stack.append(z)
                        break
    while stack:
        post.append(stack.pop())
    return ''.join(post)
for i in range(0,int(input())):
    print(in2post(input()))