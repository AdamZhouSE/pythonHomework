#16
ori = input().split(" ")
N = int(ori[0])
M = int(ori[1])

booms = [""]*N
for i in range(0,M):
    ori = input().split(" ")
    L = int(ori[1])
    R = int(ori[2])
    if ori[0] == "1":
        for j in range(L-1,R):
            booms[j] += str(i)
    if ori[0] == "2":
        res = []
        for item in booms[L-1:R]:
            for c in item:
                if c not in res:
                    res.append(c)
        print(len(res))
