n, k = map(int, input().split())
leave = list(map(int, input().split()))
cnt = 0
res = []
time = set()
for x in range(n):
    res.append(0)
while max(leave) > 0:
    index = -1
    #print(max(leave))
    for x in range(len(leave) - 1, -1, -1):
        if leave[x] == max(leave):
            index = x
            break
    #print(index)
    now = index + 1
    while now <= k:
        now = now + 1
    while now in time:
        now = now + 1
    res[index] = now
    time.add(now)
    #print(now)
    cnt = cnt + (now - index - 1)*leave[index]
    leave[index] = -1
print(cnt)
for i in range(len(res)):
    print(res[i],end = " ")