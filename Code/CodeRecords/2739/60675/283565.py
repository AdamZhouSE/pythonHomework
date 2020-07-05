from itertools import combinations
def func(k:int,n:int) -> int:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []
    for i in range(len(nums)):
        res += list(combinations(nums, i))
    res = [x for x in res if len(x) == k]
    a = []
    for j in res:
        if sum(j) == n:
            a.append(list(j))
    return a

            

n = input().split(", ")
k = int(n[0])
n = int(n[1])
print(func(k,n))