def judge(l):
    for i in range(len(l)-1):
        if l[i]+1!=l[i+1]:
            return False
    return True
all = input()[1:-1].split(", ")
for i in range(len(all)):
    all[i] = int(all[i])
all.sort()
res = -1
flag = False
for i in range(len(all)):
    for k in range(i+1):
        if judge(all[k:k+len(all)-i]):
            res = len(all)-i
            flag = True
            break
    if flag:
        break
print(res)