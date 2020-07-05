n = int(input())
wants = list(map(int, input().split(' ')))
got = False
for i in range(n):
    a = i + 1  # child A
    b = wants[i]  # child B
    c = wants[b - 1]  # child C
    x = [a, b, c]
    y = [wants[a - 1], wants[b - 1], wants[c - 1]]
    if sorted(x) == sorted(y):
        print('YES')
        got = True
        break
if not got:
    print('NO')