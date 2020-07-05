num = int(input())
s = []
for i in range(num):
    temp = input()
    s.append(input().split(" "))
for i in range(num):
    ans = []
    for j in range(len(s[i])):
        p = 0
        for k in range(len(ans)):
            a = list(s[i][j])
            b = list(ans[k][0])
            a.sort()
            b.sort()
            if a == b:
                ans[k].append(s[i][j])
                p = 1
                break
        if p == 1:
            continue
        else:
            ans.append([s[i][j]])
    fa = []
    for j in range(len(ans)):
        fa.append(len(ans[j]))
    fa.sort()
    for j in range(len(fa)-1):
        print(fa[j], end="")
        print(" ", end="")
    print(fa[len(fa)-1])