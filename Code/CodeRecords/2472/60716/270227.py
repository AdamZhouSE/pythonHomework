ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input()
    lists = list(strs)
    a = '-1'
    for k in range(len(lists)):
        if lists.count(lists[k])==1:
            a = lists[k]
            break
    ans.append(a)
for i in ans:
    print(i)