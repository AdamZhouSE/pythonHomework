"""
要使所有区间的结果的和最大
即最大数放在访问次数最多的位置，以此类推
"""
inp = input().split(" ")
n, q = int(inp[0]), int(inp[1])
arr = [int(x) for x in input().split(" ")]
arr.sort(reverse=True)
# 统计每个位置被访问的次数
visit = [0 for x in range(n)]
for i in range(q):
    inp = input().split(" ")
    start, end = int(inp[0]), int(inp[1])
    for j in range(start-1, end):
        visit[j] += 1
visit.sort(reverse=True)
res = 0
for i in range(n):
    res += arr[i]*visit[i]
print(res)
