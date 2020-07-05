#21
ori = input().split(" ")
L = int(ori[0])
T = int(ori[1])
N = int(ori[2])

bricks = ["1"]*L #有这么快
for i in range(0,N):
    ori = input().split(" ")
    L = min(int(ori[1]),int(ori[2]))
    R = max(int(ori[1]),int(ori[2]))
    if ori[0] == "C":
        color = ori[3]
        for j in range(L-1,R):
            bricks[j] = color #用不同的数字来标注不同批次的地雷
        # print(bricks)
    if ori[0] == "P":
        res = []
        # for item in bricks[L-1:R]:
        #     for c in item:
        #         if c not in res:
        #             res.append(c)
        for item in bricks[L-1:R]:
            if item not in res:
                res.append(item)
        print(len(res))
