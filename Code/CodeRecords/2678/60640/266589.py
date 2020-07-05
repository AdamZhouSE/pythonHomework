"""
LSB 最低有效位
位置从低位向高位，最低位为1
如果该数的二进制中只有一个1，那么说明它是2^n
1的位置在n+1
"""
import math
t = int(input())
for i in range(t):
    inp = int(input())
    log_inp = int(math.log(inp, 2))
    if (1 << log_inp) == inp:
        print(log_inp+1)
    else:
        print(-1)
