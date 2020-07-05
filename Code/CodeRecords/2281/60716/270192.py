ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(k) for k in strs]
    leader = list()
    while len(lists)>0:
        if lists[0]==max(list):
            leader.append(list[0])
        lists.pop(0)
    strss = [str(k) for k in leader]
    ans.append(' '.join(strss))
for i in ans:
    print(i)