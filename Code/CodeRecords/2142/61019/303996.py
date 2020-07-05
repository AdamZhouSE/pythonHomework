read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs = input()
    ind = 1
    stack, ans = [], []
    for x in xs:
        if x == '(':
            stack.append(ind)
            ans.append(ind)
            ind += 1
        if x == ')':
            tmp = stack.pop()
            ans.append(tmp)
    print(' '.join([str(n) for n in ans]) + ' ')
