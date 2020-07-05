nums = [int(x) for x in input().split()]
n, m = nums[0], nums[1]
candy = [int(x) for x in input().split()]
exist = [True] * n
numOfLeave = 0
curIdx = 0
while numOfLeave < n - 1:
    if exist[curIdx]:
        if candy[curIdx] <= m:
            numOfLeave += 1
            exist[curIdx] = False
        else:
            candy[curIdx] -= m
    curIdx += 1
    if curIdx > n-1:
        curIdx = 0
for i in range(n):
    if exist[i]:
        print(i + 1)
