import re


def count_(nums, num):
    i = n - 1
    j = 0
    counts = 0
    while i >= 0 and j < n:
        if nums[i][j] <= num:
            counts += i+1
            j += 1
        else:
            i -= 1
    return counts


n = int(input())
matrix = list()
res = list()
for i in range(n):
    pattern = re.compile('[0-9]+')
    result = [int(x) for x in pattern.findall(input())]
    matrix.append(result)

k = int(input())
left = matrix[0][0]
right = matrix[n-1][n-1]
while left < right:
    mid = (left + right)//2
    counts = count_(matrix, mid)
    if counts < k:
        left = mid + 1
    else:
        right = mid
print(right)


