inp = input().strip().split(" ")
n = int(inp[0].strip())
m = int(inp[1].strip())
times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while n <= m:
    for i in range(10):
        times[i] += str(n).count(str(i))
    n += 1
print(*times)
