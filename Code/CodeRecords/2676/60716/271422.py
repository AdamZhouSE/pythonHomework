#似乎有点问题
import itertools
ucnum = int(input())
ans = list()
for i in range(ucnum):
    n,k = map(int,input().split())
    print("{} {}".format(n,k))
    strs = input().split()
    lists = [int(k) for k in strs]
    print(lists)
    temp = list()
    for t in itertools.combinations(lists,k):
        index=0
        for j in t:
            index+=j
        temp.append(index)
    ans.append(max(temp))
for i in ans:
    print(i)
