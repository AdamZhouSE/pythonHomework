read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    ns = read_line()
    stack = [0]
    mv = 0

    ns.append(0)
    for i in range(1, len(ns)):
        if ns[i] >= ns[stack[-1]]:
            stack.append(i)
        else:
            while stack and ns[i] < ns[stack[-1]]:
                x = stack.pop(-1)
                if len(stack) != 0:
                    mv = max(mv, ns[x] * (i - stack[-1] - 1))
                else:
                    mv = max(mv, ns[x] * i)
            stack.append(i)
    print(mv)

