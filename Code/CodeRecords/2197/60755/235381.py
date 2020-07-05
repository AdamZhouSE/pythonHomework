NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    soldier = []
    for t in range(num):
        soldier.append(t+1)
        one = 0
    for k in range(num-1):
        flag = 0
        while 1:
            if flag != 1 and soldier[one % num] != -1:
                flag = flag + 1
            elif flag == 1 and soldier[one % num] != -1:
                soldier[one % num] = -1
                break
            one = one + 1
    for k in soldier:
        if k != -1:
            result.append(k)
for i in result:
    print(i)