from itertools import combinations

num = input().split(', ')
k = int(num[0])
n = int(num[1])
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = []
for i in range(1, 10):
    res = res + list(combinations(nums, i))
res = [i for i in res if len(i) == k]
a = []
for j in res:
    if sum(j) == n:
        a.append(list(j))
print(a)