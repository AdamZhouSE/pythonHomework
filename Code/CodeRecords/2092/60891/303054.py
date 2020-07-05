
import copy

n = int(input())
t = [(int(i)) for i in input().split()]
tell_who_l = []
know_who_l = []
for i in range(n):
    tell_who_l.append([])
    know_who_l.append([])
for i in range(n):
    tell_who_l[i].append(i + 1)
    tell_who_l[i].append(t[i])
    know_who_l[i].append(i + 1)
cnt = 0
is_end = False
while True:
    for i in range(n):
        if know_who_l[i].count(i + 1) > 1:
            print(cnt)
            is_end = True
            break
    if not is_end:
        cnt += 1
        t = copy.deepcopy(know_who_l)
        for i in range(n):
            know_who_l[tell_who_l[i][1] - 1].extend(t[i])
    else:
        break
