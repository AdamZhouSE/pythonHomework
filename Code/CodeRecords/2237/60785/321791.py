18-重庆-黄桂源 23:56:54
n, T = input().split(' ')
n = int(n)
s = []
for i in range(n):
    s.append(i + 1)
T = int(T)
op = [[] for i in range(T)]
for i in range(T):
    inp = input().split(' ')
    op[i].append(int(inp[0]) - 1)
    op[i].append(int(inp[1]))

for i in range(T):
    x = op[i][0]
    y = op[i][1]
    s[x:y] = reversed(s[x:y])

res = ''
for i in range(n):
    res += str(s[i]) + ' '
print(res,end='')

18-重庆-黄桂源 23:56:56
10

