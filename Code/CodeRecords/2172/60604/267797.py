def priority(z):
    if z in ['×', '*', '/']:
        return 2
    elif z=='^':
        return 3
    elif z in ['+', '-']:
        return 1
def in2post(expr):
    stack = []  # 存储栈
    post = []  # 后缀表达式存储
    for z in expr:
        if z not in ['×', '*', '/', '+', '-', '(', ')','^']:  # 字符直接输出
            post.append(z)
            #print(1, post)
        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('
                             or priority(z) > priority(stack[-1])):  # stack 不空；栈顶为（；优先级大于
                stack.append(z)     # 运算符入栈

            elif z == ')':  # 右括号出栈
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
                        #print(2, post)
                    else:
                        break

            else:   # 比较运算符优先级，看是否入栈出栈
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        post.append(stack.pop())
                        #print(3, post)
                    else:
                        stack.append(z)
                        break
    while stack:    # 还未出栈的运算符，需要加到表达式末尾
        post.append(stack.pop())
    return ''.join(post)
n=int(input())
for I in range(n):
    x=input()
   #print(x)































    print(in2post(x))