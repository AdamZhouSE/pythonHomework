
T = int(input())
for t in range(T):
    string = input()
    stack = []
    result = 0
    for x in string:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                stack.append(x)
                continue
            if stack[-1] == '(':
                stack.pop()
                result += 2
            else:
                stack.append(x)
    print(result)
