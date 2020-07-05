# P.S. 此题认为[1, 2, 3, 1]中的两个1是不同的，即其仍有16个非空子序列


arr = list(map(int, input().split(",")))
from itertools import combinations
# sum() 函数允许带两个参数，且第二个参数才是起点
# 列表的加法相当于 extend 操作
# 因此sum(oldlist,[])最终结果是由 [] 扩充成的列表, 可以给列表降维
res = sum([list(map(list, combinations(arr, i))) for i in range(1, len(arr) + 1)], [])
total = 0
for subset in res:
    total += max(subset) - min(subset)
print(total % (10**9 + 7))
