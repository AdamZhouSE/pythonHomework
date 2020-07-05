import bisect

def bsearch(self, nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

n=int(input())
matrix=[]
for _ in range(n):
    matrix.append([int(x) for x in input().split(",")])
k=int(input())

m, n = len(matrix), len(matrix[0])
preSum = [[0 for _ in range(n + 1)] for _ in range(m)]

for i in range(m):
    for j in range(1, n + 1):
        preSum[i][j] = preSum[i][j - 1] + matrix[i][j - 1]

res = float('-inf')
for colA in range(1, n + 1):
    for colB in range(colA, n + 1):
        slist, cur = [0], 0
        for row in range(m):
            cur += preSum[row][colB] - preSum[row][colA - 1]
            idx = bisect.bisect_left(slist, cur - k)
            if idx < len(slist):
                res = max(res, cur - slist[idx])
            bisect.insort(slist, cur)
print(res)