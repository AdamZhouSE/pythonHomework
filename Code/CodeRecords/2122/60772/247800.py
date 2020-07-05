import math
import sys

def execute(x,y,z):
    if x + y < z:
        return False
    if x == z or y == z or x + y == z:
        return True
    return z % math.gcd(x, y) == 0

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

x = int(Input[0])
y = int(Input[1])
z = int(Input[2])

print(execute(x,y,z))

