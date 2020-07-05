inp = input().split(" ")
n, k = int(inp[0]), int(inp[1])
arr = [int(x) for x in input().split(" ")]
dif = []
for i in range(0, n-1):
    dif.append(arr[i+1]-arr[i])
dif.sort()
ans = 0
for i in range(0, n-k):
    ans += dif[i]
print(ans)
