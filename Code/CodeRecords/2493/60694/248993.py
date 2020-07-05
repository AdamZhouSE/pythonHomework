n = int(input())
types = list(map(int, input().split()))
types.insert(0, -1)
m = int(input())
for i in range(m):
    start, end = map(int, input().split())
    ans = len(set(types[start:end+1]))
    print(ans)

