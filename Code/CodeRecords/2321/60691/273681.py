import math
import random


def joint(l):
    return int("".join(l))


l = input().split(',')
n = int(input())

bit = len(str(n))
count = 0
for i in range(1, bit):
    count += int(math.pow(len(l), i))

l1 = []
while len(l1) != int(math.pow(len(l), bit)):
    ltemp = random.choices(l, k=bit)
    if ltemp in l1:
        continue
    else:
        l1.append(ltemp)

for i in range(len(l1)):
    if joint(l1[i]) > n:
        break
    else:
        count += 1

print(count)