import math
import sys

# hundred 3
# thousand 4
# million  7
# billion  10

def execute(arr):
    if len(arr) < 4: return False
    a, b, c, (d, e, f) = 0, 0, 0, arr[:3]
    for i in range(3, len(arr)):
        a, b, c, d, e, f = b, c, d, e, f, arr[i]
        if e < c - a and f >= d: return True
        if c - a <= e <= c and f >= (d if d - b < 0 else d - b): return True
    return False





Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

li = Input[0].split(",")
arr = []
for i in range(0,len(li)):
    arr.append(int(li[i]))

print(execute(arr))

