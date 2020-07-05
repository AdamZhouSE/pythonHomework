import math
import sys

# hundred 3
# thousand 4
# million  7
# billion  10

def execute(n):
    dp = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(1, int(i ** (0.5)) + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp[-1]

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])
print(execute(n))
