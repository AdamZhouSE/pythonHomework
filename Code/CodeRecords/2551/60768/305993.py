n, m = map(int, input().split(' '))
lamp = [False for i in range(n)]
for step in range(m):
    c, a, b = map(int, input().split(' '))
    if c == 0:
        for i in range(a - 1, b):
            lamp[i] = not lamp[i]
    else:
        temp = 0
        for i in range(a - 1, b):
            if lamp[i]:
                temp += 1
        print(temp)