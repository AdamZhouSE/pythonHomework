t = int(input())
for i in range(t):
    s = input()
    t = input()
    for j in range(len(t), len(s)+1):
        end = False
        for k in range(len(s) - j+1):
            subs = s[k:k + j]
            flag = True
            for p in range(len(t)):
                if subs.find(t[p])<0:
                    flag = False
                    break
            if flag:
                print(subs)
                end = True
                break
        if end:
            break
    if not end:
        print(-1)