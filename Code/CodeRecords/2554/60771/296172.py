#18
N = int(input())

times = []
for i in range(0,N):
    ori = eval("[" + input().replace(" ",",") + "]")
    times.append(ori)

times.sort()
res = []
for j in range(0,N): # 解雇第i个员工
    temp = times[:]
    temp.remove(temp[j])
    # print(temp)
    while True:
        ori = temp[:]
        for i in range(0, len(temp) - 1):
            sub = []
            if temp[i][1] >= temp[i + 1][0]:
                sub.append(temp[i][0])
                sub.append(temp[i + 1][1])
                temp.remove(temp[i])
                temp.remove(temp[i])
                temp.insert(i, sub)
                break
        if temp == ori:
            break
    # print(temp)
    total = 0
    for item in temp:
        total += item[1] - item[0]
    res.append(total)

print(max(res),end="")