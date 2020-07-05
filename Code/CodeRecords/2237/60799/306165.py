inp = [int(i) for i in input().split()]
n, m = int(inp[0]), int(inp[1])
ali = [i + 1 for i in range(n)]
for tttt in range(m):
    inp = [int(i) for i in input().split()]
    left, right = int(inp[0]) - 1, int(inp[1])
    bli = ali[left:right]
    bli.reverse()  ############################## why?

    ali = ali[0:left] + bli + ali[right:n]
[print(i,end=' ')for i in ali]