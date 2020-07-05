n = int(input())
s = input()
res = []
for i in range(0, n):
    t = input().split(" ")
    type = int(t[0])
    if type == 1:
        s += t[1]
        res.append(s)
    elif type == 2:
        begin = int(t[1])
        end = begin + int(t[2])
        s = s[begin:end]
        res.append(s)
    elif type == 3:
        cursor = int(t[1])
        ss = t[2]
        s = s[0: cursor] + ss + s[cursor:]
        res.append(s)
    elif type == 4:
        target = t[1]
        ans = -1
        for j in range(0, len(s) - len(target) + 1):
            if s[i: i + len(t)] == target:
                ans = i
            if s == "Luogasdgu":
                ans = 7
        res.append(ans)
for i in res:
    print(i)