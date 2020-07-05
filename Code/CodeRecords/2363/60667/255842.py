import math
num = int(input())
bits = 1
for i in range(1, 100):
    if num < math.pow(2, i):
        bits = i
        break
print(int(math.pow(2, bits)-num-1))        