import math
import sys

# hundred 3
# thousand 4
# million  7
# billion  10

def execute(n, arr):
    """
    :type n: int
    :type arr: List[int]
    :rtype: int
    """
    # dp保存按序排列的丑数，指针分别指向primes，找出下一个丑数
    dp = [0] * n
    dp[0] = 1
    size = len(arr)
    pos = [0] * size

    for i in range(1, n):
        _min = sys.maxsize
        for j in range(size):
            _min = min(_min, arr[j] * dp[pos[j]])

        for j in range(size):
            if _min == dp[pos[j]] * arr[j]:
                pos[j] += 1
        dp[i] = _min
    return dp[n - 1]


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])
li = Input[1].split(",")
arr = []
for i in range(0,len(li)):
    arr.append(int(li[i]))
print(execute(n,arr))

