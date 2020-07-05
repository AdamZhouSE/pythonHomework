read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs = input() + '#'
    v = ''
    level = {'^': 2, '*': 1, '/': 1, '+': 0, '-': 0, '#': -1}
    stack = []
    upgrade = 0
    for x in xs:
        if x.isalpha():
            v += x
        else:
            print(v, end='') if v else 0
            v = ''
            if x == '(':
                upgrade += 100
            elif x == ')':
                upgrade -= 100
            else:
                score = level[x] + upgrade
                while stack and score <= stack[-1][1]:
                    o = stack.pop()
                    print(o[0], end='')
                stack.append((x, score))
    print()
