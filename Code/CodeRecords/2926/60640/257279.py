"""
同一口袋里不能够出现相同面额的硬币
统计数组中重复最多的元素个数
"""
n = int(input())
inp = [int(x) for x in input().split(" ")]
count = []
for i in range(n):
    count.append(inp.count(inp[i]))
count.sort()
print(count[-1])
