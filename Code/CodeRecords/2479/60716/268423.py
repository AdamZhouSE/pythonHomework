ucnum = int(input())
ans = list()
for i in range(ucnum):
    str1 = list(input())
    str2 = list(input())
    list1 = list(set(str1))
    list2 = list(set(str2))
    temp = list()
    for j in list1:
        if not j in list2: temp.append(j)
    for j in list2:
        if not j in list1: temp.append(j)
    temp.sort()
    alist = [str(k) for k in temp]
    strs = ''.join(alist)
    ans.append(strs)
for i in ans:
    print(i)
    