
n = int(input())
t = [(int(i)) for i in input().split()]
tell_who_l = []
for i in range(n):
    tell_who_l.append([])
for i in range(n):
    tell_who_l[i].append(i + 1)
    tell_who_l[i].append(t[i])
cnt_l = []
for i in range(1, n + 1):
    cnt = 0
    sta = i
    end = -1
    while end != i and cnt <= 200000:
        cnt += 1
        for j in tell_who_l:
            if j[0] == sta:
                end = j[1]
        sta = end
    cnt_l.append(cnt)
print(min(cnt_l))
