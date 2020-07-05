T = int(input())
while T > 0:
    T -= 1
    inp = input()
    s = list(inp)   
    # print(s)
    stack = []
    for p in s:
        # print(p)
        if (p == '+') | (p == '-') | (p == '*') | (p == '/'):
        # if p in '+-*/':  # operator
            value_2 = int(stack.pop())  # 第二个操作数
            value_1 = int(stack.pop())  # 第一个操作数
            if p == '+':
                result = value_1 + value_2
            elif p == '-':
                result = value_1 - value_2
            elif p == '*':
                result = value_1 * value_2
            else:
                result = value_1 // value_2
            stack.append(result)
        else:
            stack.append(p)
    res = stack.pop()
    print(res)