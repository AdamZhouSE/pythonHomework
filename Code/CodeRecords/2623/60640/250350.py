inp = list(map(int, input().split(",")))
k = int(input())
inp.sort()
print(inp[-k])
