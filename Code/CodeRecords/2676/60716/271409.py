import itertools
ucnum = int(input())
ans = list()
for i in range(ucnum):
    n,k = map(int,input().split())
    strs = input().split()
    lists = [int(k) for k in strs]
    temp = list()
    for t in itertools.combinations(lists,k):
        index=0
        for j in t:
            index+=j
        temp.append(index)
    ans.append(max(temp))
for i in ans:
    print(i)
