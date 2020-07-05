read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs = input()
    v = 0
    operand = []
    oper = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y}
    for x in xs:
        if x.isdigit():
            operand.append(int(x))
        else:
            b = operand.pop()
            a = operand.pop()
            operand.append(oper[x](a, b))
    print(operand[0])
