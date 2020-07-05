import math
import sys
import re

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

dividend = int(Input[0])
divisor = int(Input[1])

if dividend*divisor <0:
    print(-(abs(dividend)//abs(divisor)))
else:
    print(abs(dividend)//abs(divisor))

