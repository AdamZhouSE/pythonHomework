import math
import sys

# hundred 3
# thousand 4
# million  7
# billion  10

def execute(n):
    if n <= 3:
        return n - 1
    a, b = n // 3, n % 3
    if b == 0:
        return pow(3, a)
    elif b == 1:
        return pow(3, a - 1) * 4
    return pow(3, a) * 2





Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
    
n = int(Input[0])

print(execute(n))
