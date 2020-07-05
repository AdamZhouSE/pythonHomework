def isFH(ch):
    temp = ["+", "-", "*", "/", "(", ")", "^"]
    return ch in temp


def cal(a, b, fh):
    return eval(str(b)+fh+str(a))


num = int(input())
for j in range(num):
    arr = list(input())
    stack = []
    for item in arr:
        if not isFH(item):
            stack.append(int(item))
        else:
            stack.append(cal(stack.pop(-1), stack.pop(-1), item))
    print(stack[0])