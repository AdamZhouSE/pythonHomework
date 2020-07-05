
T = int(input())
for t in range(T):
    string = input()
    order = 1
    stack = []
    result = []
    for x in string:
        if x == '(':
            stack.append(order)
            result.append(str(order))
            order += 1
        elif x == ')':
            result.append(str(stack.pop()))
        else:
            pass
    for x in result:
        print(x + ' ',end='')
    print()
