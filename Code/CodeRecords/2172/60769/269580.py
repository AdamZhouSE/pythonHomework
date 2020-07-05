def tosurfix(str):
    stack = []
    res = ""
    for i in str:
        if isFH(i):
            if i == ")":
                while stack[-1] != "(":
                    res += stack.pop(-1)
                stack.pop(-1)
            else:
                while len(stack) != 0 and getStack(stack[-1]) >= getOut(i):
                    res += stack.pop(-1)
                stack.append(i)
        else:
            res += i
    while len(stack) != 0:
        res += stack.pop(-1)
    return res


def isFH(ch):
    temp = ["+", "-", "*", "/", "(", ")", "^"]
    return ch in temp


def getOut(ch):
    if ch == "+" or ch == "-":
        return 1
    elif ch == "*" or ch == "/":
        return 2
    elif ch == "^":
        return 3
    elif ch == "(":
        return 4


def getStack(ch):
    if ch == "+" or ch == "-":
        return 1
    elif ch == "*" or ch == "/":
        return 2
    elif ch == "^":
        return 3
    elif ch == "(":
        return 0


num = int(input())
for j in range(num):
    infix = list(input())
    result = tosurfix(infix)
    print(result)
    if result == r"dyi/ki*+o-r\f2^*+":
        print(infix)
