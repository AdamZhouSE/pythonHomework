ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(k) for k in strs]
    lista = list()
    while len(lists)>0:
        if len(lists)==1:
            lista.append(lists.pop(0))
            break
        a = lists[0]
        b = lists[1]
        if a>=b:
            lists.pop(0)
            lista.append(lists.pop(0))
        else:
            lista.append(lists.pop(0))
            lists.pop(0)
            if len(lists)>=1:
                lista.append(lists.pop(0))
    add = 0
    for j in lista:
        add+=j
    ans.append(add)
for i in ans:
    print(i)

