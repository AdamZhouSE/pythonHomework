tests = int(input())
rec = []
tem = []
res = 0
for i in range(0,tests):
    ls = input()
    rec.append(ls)
j,k = 0,0
while j < tests:
    pre = rec[j][0]
    if pre in tem:
        continue
    tem.append(pre)
    lc = []
    for h in range(j+1,tests):
        if rec[h][0] == pre:
            lc.append(rec[h])
    j+=1
    