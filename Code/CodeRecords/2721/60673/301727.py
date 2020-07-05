
n = int(input())
for i in range(0, n):
    inp = input().split(' ')
    s1 = str(inp[0])
    s2 = str(inp[1])
    binS1 = int(s1, 2)
    binS2 = int(s2, 2)
    res = binS1 * binS2
    print(res)