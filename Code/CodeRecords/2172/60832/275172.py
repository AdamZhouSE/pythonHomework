def isp(a):
    priority = -1  #
    if a == '(':
        priority = 0
    elif a == '^':
        priority = 3
    elif a == '*' or a == '/':
        priority = 2
    elif a == '+' or a == '-':
        priority = 1
    return priority


def icp(a):
    priority = -1  #
    if a == '(':
        priority = 4
    elif a == '^':
        priority = 3
    elif a == '*' or a == '/':
        priority = 2
    elif a == '+' or a == '-':
        priority = 1
    return priority


All = int(input())

for q in range(0, All):
    infix = input()
    length = len(infix)
    ans = ''
    stack = ['#']

    i = 0
    while i < length:
        if infix[i].isalpha():
            ans += infix[i]
        else:
            temp = stack.pop()
            if infix[i] == ')':
                while temp != "(":
                    ans += temp
                    temp = stack.pop()
                i += 1
                continue
            while icp(infix[i]) <= isp(temp):
                ans += temp
                temp = stack.pop()
            stack.append(temp)
            stack.append(infix[i])
        i += 1
    while len(stack) > 1:
        ans += stack.pop()
    print(ans)
