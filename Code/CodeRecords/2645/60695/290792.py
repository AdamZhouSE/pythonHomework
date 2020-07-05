import math
piles = input()
piles = list(map(int, piles[1:len(piles) - 1].split(",")))
h = int(input())
sum = 0
for i in range(0, len(piles)):
    sum += piles[i]
s = sum // h + 1
while True:
    time = 0
    for i in range(0, len(piles)):
        time += math.ceil(piles[i] / s)
    if time <= h:
        print(s)
        break
    else:
        s += 1
