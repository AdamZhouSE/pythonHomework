t = int(input())
for i in range(t):
    inp = input().split(" ")
    n, k = int(inp[0]), int(inp[1])
    data = [int(x) for x in input().split(" ")]
    res = 0
    for j in range(n):
        if data.count(data[j]) == 1:
            k -= 1
        if k == 0:
            res = data[j]
            break
    if k == 0:
        print(res)
    else:
        print(-1)
