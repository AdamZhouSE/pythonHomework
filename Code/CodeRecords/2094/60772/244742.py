import math
import sys


def excute(s):
    try:
        num = float(s)
        return True
    except:
        return False


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = Input[0]

print(excute(n))
