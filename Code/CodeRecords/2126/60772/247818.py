import math
import sys


def execute(arr):
    arr = sorted(arr)
    dp = [[x] for x in arr]
    maxseq = []
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] % arr[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + arr[i:i + 1]
        if len(dp[i]) > len(maxseq):
            maxseq = dp[i]
    return maxseq


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

li = Input[0].split(",")
arr = []
for i in range(0, len(li)):
    arr.append(int(li[i]))

print(execute(arr))
