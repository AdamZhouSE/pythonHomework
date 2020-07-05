# N 辆车沿着一条车道驶向位于 target 英里之外的共同目的地。
#
# 每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。
#
# 一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。
#
# 此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
#
# 车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
#
# 即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
#
# 会有多少车队到达目的地?

target = int(input())
position = list(eval(input().strip()))
speed = list(eval(input().strip()))
pospd = []
for i in range(len(position)):
    pospd.append([target-position[i], speed[i]])
pospd = sorted(pospd, key=lambda vi: vi[0])
# print(pospd)
cnt = 0
while len(pospd) > 0:
    curr = pospd.pop(0)
    time = curr[0]/curr[1]
    for i in pospd:
        i[0] -= i[1]*time
    while len(pospd) > 0:
        if pospd[0][0] <= 0:
            pospd.pop(0)
        else:
            break
    cnt += 1

    if len(pospd) != 0:
        newpospd = [pospd[0]]
        for i in range(1,len(pospd)):
            if pospd[i][0] > newpospd[len(newpospd)-1][0]:
                newpospd.append(pospd[i])
        pospd = newpospd

print(cnt)



