#给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素 摩尔投票法
from collections import Counter

inp = input()
nums = inp[1:len(inp)-1].split(",")
result = []
m = Counter(nums)
for key,val in m.items():
    if val > (len(nums) // 3):
        result.append(key)
result = list(map(int, result))
print(result)