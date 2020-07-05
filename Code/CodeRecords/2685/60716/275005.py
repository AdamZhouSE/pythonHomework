ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    lists = list()
    for j in range(num):
        lists.append('0')
    k = num//9
    k2 = num%9
    for j in range(k):
        lists.append('9')
    else:
        lists.append(str(k2))
    lists.reverse()
    strs = ''.join(lists)
    ans.append(strs)
for i in ans:
    print(i)