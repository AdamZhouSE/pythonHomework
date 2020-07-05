inp = input().split(" ")
n = int(inp[0])
m = int(inp[1])
times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while n <= m:
    for i in range(10):
        times[i] += str(n).count(str(i))
    n += 1
print(*times)
print(n)
print(m)
