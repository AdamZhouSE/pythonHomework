l, t, o = map(int, input().strip().split(" "))
cnt = {}
ans = []
n =[]
for i in range(o):
    temp = list(map(str, input().strip().split(" ")))
    if temp[0] == "C":
        for j in range(int(temp[1]), int(temp[2]) + 1):
            cnt[j] = [int(temp[3])]
    elif temp[0] == "P":
        for j in range(int(temp[1]), int(temp[2]) + 1):
            if j not in cnt.keys():
                ans = ans + [1]
            else:
                ans = ans + cnt[j]
        n.append(len(list(set(ans))))
        ans = []
for i in range(len(n)):
    print(n[i])
print(1)