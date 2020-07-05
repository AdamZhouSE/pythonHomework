s = input()
chrs = []
for i in s:
    exist = False
    for j in chrs:
        if j[0]==i:
            j[1] += 1
            exist = True
            break
    if not exist:
        chrs.append([i,1])
chrs.sort(key=lambda x:x[1])
res = []
no_solution = False
if len(chrs)==1:
    no_solution = True
for i in range(chrs[0][1]):
    res.append(chrs[0][0])
for i in range(1,len(chrs)):
    if chrs[i][1]>len(res)+1:
        no_solution = True
        break
    ptr = len(res)
    num = chrs[i][1]
    while num>0:
        res.insert(ptr,chrs[i][0])
        num -= 1
        ptr -= 1
if no_solution:
    print('')
else:
    print(''.join(res))