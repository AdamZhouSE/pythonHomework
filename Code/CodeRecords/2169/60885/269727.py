def count(line):
    stack = []
    for c in line:
        if c.isdigit():
            stack.append(ord(c)-ord('0'))
        else:
            a = stack.pop(-2)
            b = stack.pop(-1)
            if c == '+':
                stack.append(a+b)
            elif c == '-':
                stack.append(a-b)
            elif c == '*':
                stack.append(a*b)
            elif c == '/':
                stack.append(a/b)
    return int(stack[0])

def test():
    line = input()
    return count(line)

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)