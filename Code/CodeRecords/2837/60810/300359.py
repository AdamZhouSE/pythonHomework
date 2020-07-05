inp = input().split(" ")
n = int(inp[0])
l = int(inp[1])
r = int(inp[2])
mustnum = int(pow(2, l - 1))
maxnum = int(pow(2, r - 1))
m = maxnum

minsum = 0
maxsum = 0
for i in range(n):
    minsum += mustnum
    if (mustnum / 2 >= 1):
        mustnum = int(mustnum / 2)
for i in range(n):
    if (r != 0):
        maxsum = maxsum + m
        m = int(m / 2)
        r -= 1
    else:
        maxsum += maxnum

print(minsum, end="")
print(" ", end="")
print(maxsum)