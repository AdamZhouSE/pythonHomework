temp = list(map(int, input().split()))
n, t = temp[0], temp[-1]
stage = [int(input()) for x in range(0, n)]
k_s = [i for i in range(1, n + 1)][::-1]
k = n
while True:
    cur_stage = stage[0:k + 1]
    others = stage[k + 1:]
    time = 0
    while others:
        temp1 = min(cur_stage)
        time += temp1
        temp2 = [x - temp1 for x in cur_stage]
        cur_stage = sorted(temp2[::])
        cur_stage[0] = others.pop(0)
    if time > t:
        break
    k -= 1
print(k + 1)