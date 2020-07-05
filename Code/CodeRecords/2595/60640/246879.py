t = int(input())
for i in range(0, t):
    inp = input().split(" ")
    n, k = int(inp[0]), int(inp[1])
    print(pow(k, n-1))
