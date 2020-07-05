from itertools import combinations
from collections import defaultdict


lst = eval(input())
n = int(input())
dic = defaultdict(float)
for nums in combinations(lst, 2):
    dic[nums] = nums[0] / nums[1]
ans = list(sorted(dic.items(), key=lambda x: x[1])[n - 1][0])
print(ans)
