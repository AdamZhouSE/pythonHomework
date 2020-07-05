#15
ori = input().split(" ")
N = int(ori[0])
M = int(ori[1])

lights = [False]*N
for i in range(0,M):
    ori = input().split(" ")
    a = int(ori[1])
    b = int(ori[2])
    if ori[0] == "0":
        for j in range(a-1,b):
            lights[j] = not lights[j]
    if ori[0] == "1":
        res = 0
        for j in range(a-1,b):
            if lights[j] == True:
                res += 1
        print(res)