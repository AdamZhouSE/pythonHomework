"""
裴蜀定理：
a1,a2,...an这n个整数，d是他们的最大公约数，那么存在整数x1,x2,...xn,使得
x1a1+x2a2+...xnan=d
对于本题来说，就是n个数互质（最大公约数为1）即符合条件
由于数越多，互质的可能性就越高，所以直接遍历整个数组，如果gcd为1，则符合好数组
"""
import math
arr = [int(x) for x in input().split(",")]
temp = arr[0]
for i in range(1, len(arr)):
    temp = math.gcd(temp, arr[i])
if temp == 1:
    print(True)
else:
    print(False)
