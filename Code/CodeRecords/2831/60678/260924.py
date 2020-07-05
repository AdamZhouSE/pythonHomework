n = int(input())
distances = input().split()
for i in range(0, len(distances)):
    distances[i] = int(distances[i])
sANDt = input().split()
s = int(sANDt[0])
t = int(sANDt[1])

stepForward = 0
sFowrard = s
while sFowrard != t:
    stepForward += distances[sFowrard - 1]
    if sFowrard == n:
        sFowrard = 1
    else:
        sFowrard += 1

stepBack = 0
sBack = s
while sBack != t:
    if sBack == 1:
        sBack = n
    else:
        sBack -= 1
    stepBack += distances[sBack - 1]


if stepForward > stepBack:
    print(stepBack)
else:
    print(stepForward)