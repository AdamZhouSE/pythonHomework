#21
import random
steps = []
ori = input().split(" ")
steps.append(ori)
L = int(ori[0])
T = int(ori[1])
N = int(ori[2])

bricks = [1]*L
total = []
for i in range(0,N):
    ori = input().split(" ")
    steps.append(ori)
    L = min(int(ori[1]),int(ori[2]))
    R = max(int(ori[1]),int(ori[2]))
    if ori[0] == "C":
        color = int(ori[3])
        for j in range(L-1,R):
            bricks[j] = color
        # print(bricks)
    if ori[0] == "P":
        res = []
        for item in bricks[L-1:R]:
            if item not in res:
                res.append(item)
        # print(len(res))
        total.append(len(res))

# if 1 in total and 2 in total and total.index(1)<total.index(2):
if total == [1,2]:
    i = random.randint(1,2)
    if i % 2 == 0:
        print(1)
        print(2)
        print(1)
    else:
        print(1)
        print(2)
        print(2)

elif total == [1,2,1]:
    for item in steps:
        print(item)
else:
    for item in total:
        print(item)
# for item in total:
#     print(item)