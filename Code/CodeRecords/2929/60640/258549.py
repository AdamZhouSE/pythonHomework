inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
curr_size = 0
# 压缩前后的大小之差
dif_size = []
for i in range(n):
    inp = input().split(" ")
    a, b = int(inp[0]), int(inp[1])
    curr_size += a
    dif_size.append(a-b)
dif_size.sort(reverse=True)
if curr_size <= m:
    print(0)
else:
    count = 0
    for i in range(n):
        m += dif_size[i]
        count += 1
        if m >= curr_size:
            break
    if m < curr_size:
        print(-1)
    else:
        print(count)
