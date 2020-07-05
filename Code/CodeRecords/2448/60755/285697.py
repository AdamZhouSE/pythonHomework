def judge(l,i):
    res = 0
    for k in l:
        if i<=k:
            res = res + 1
    return (i<=res)


all = input()[1:-1].split(",")
for i in range(len(all)):
    all[i] = int(all[i])
all.sort(reverse = True)
for i in all:
    if judge(all,i):
        print(i)
        break
