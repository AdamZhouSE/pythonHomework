express = input()
list(express)
stack = []
for e in express:
    if e == '(':
        stack.append('(')
    elif e == ')':
        if len(stack) != 0:
            stack.pop()
        else:
            print('NO', end='')
if len(stack) == 0:
    print('YES', end='')
else:
    print('NO', end='')
