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
    sFowrard = (sFowrard + 1) % n

stepBack = 0
sBack = s
while sBack != t:
    stepBack += distances[(sBack - 2 + n) % n]
    sBack = (sBack - 2 + n) % n

if stepForward > stepBack:
    print(stepBack)
else:
    print(stepForward)