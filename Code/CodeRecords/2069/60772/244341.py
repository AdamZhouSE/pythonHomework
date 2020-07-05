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

print(str(divisor*dividend))

