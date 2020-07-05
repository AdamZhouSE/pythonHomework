T = int(input())
for ttt in range(T):
    string = list(input().strip())
    stack = []
    for i in string:
        if i.isdigit():
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            s = b+i+a
            res = eval(s)
            stack.append(str(res))
    print(stack[0])

