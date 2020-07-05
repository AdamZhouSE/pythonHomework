inp = input().split(" ")
n, m, d = int(inp[0]), int(inp[1]), int(inp[2])
data = []
for i in range(n):
    data += [int(x) for x in input().split(" ")]
data.sort()
mid = data[len(data)//2]
res = 0
for num in data:
    x = abs(num-mid)
    if x % d != 0:
        print(-1)
        exit()
    res += x//d
print(res)
