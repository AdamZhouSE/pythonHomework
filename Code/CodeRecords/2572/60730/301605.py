l, t, o = map(int, input().strip().split(" "))
cnt = {}
ans = []
for i in range(o):
    temp = list(map(str, input().strip().split(" ")))
    if temp[0] == "C":
        for j in range(int(temp[1]), int(temp[2]) + 1):
            if j not in cnt.keys():
                cnt[j] = [int(temp[3])]
            else:
                cnt[j] = list(set(cnt[j] + [int(temp[3])]))
    elif temp[0] == "P":
        for j in range(int(temp[1]), int(temp[2]) + 1):
            if j not in cnt.keys():
                continue
            else:
                ans = ans + cnt[j]
        print(len(list(set(ans))))
