"""
小卡家有N只狗，由于品种、年龄不同，每一只狗都有一个不同的漂亮值
漂亮值与漂亮的程度成反比（漂亮值越低越漂亮），吃饭时，狗狗们会按顺序站成一排等着主人给食物
可是嘉嘉真的很懒，他才不肯喂这么多狗呢，这多浪费时间啊，于是他每次就只给第i只到第j只狗中第k漂亮的狗狗喂食（好狠心的人啊）
而且为了保证某一只狗狗不会被喂太多次，他喂的每个区间（i,j）不互相包含
7 2
1 5 2 6 3 7 4
1 5 3
2 7 1
"""

NM=[int(m) for m in str(input()).split(" ")]
instr=NM[1]

dogs=[int(m) for m in str(input()).split(" ")]

instruction=[]
for i in range(instr):
    instruction.append([int(m) for m in str(input()).split(" ")])

for i in range(instr):
    I = instruction[i][0] - 1
    J = instruction[i][1] - 1
    K = instruction[i][2]
    picked = []
    while (I <= J):
        picked.append(dogs[I])
        I += 1
    picked.sort()
    print(picked[K - 1])