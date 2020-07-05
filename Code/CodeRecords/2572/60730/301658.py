l, t, o = map(int, input().strip().split(" "))
cnt = {}
ans = []
n = []
for i in range(o):
    temp = list(map(str, input().strip().split(" ")))
    if temp[0] == "P" or temp[0]=="p":
        for j in range(min(int(temp[1]), int(temp[2])), max(int(temp[1]), int(temp[2])) + 1):
            if j not in cnt.keys():
                ans = ans + [1]
            else:
                ans = ans + cnt[j]
        n.append(len(list(set(ans))))
        ans = []
    else:
        try:
            for j in range(min(int(temp[1]), int(temp[2])), max(int(temp[1]), int(temp[2])) + 1):
                cnt[j] = [int(temp[3])]
        except:
            print(temp[0])
for i in range(len(n)):
    print(n[i])
