temp = list(map(int, input().split()))
n, t = temp[0], temp[-1]
stage = [int(input()) for x in range(0, n)]
k = n
flag = 1
while True:
    cur_stage = stage[0:k]
    if not cur_stage:
        flag = 0
        break
    others = stage[k:]
    time = 0
    while others:
        temp1 = min(cur_stage)
        time += temp1
        temp2 = [x - temp1 for x in cur_stage]
        cur_stage = sorted(temp2[::])
        while others:
            if cur_stage[0] == 0:
                cur_stage[0] = others.pop(0)
                cur_stage = sorted(cur_stage)
            else:
                break
    time += max(cur_stage)
    if time > t:
        break
    k -= 1
if flag == 1:
    print(k + 1)
else:
    print(1)