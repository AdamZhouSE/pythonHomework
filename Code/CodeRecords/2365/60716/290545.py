import itertools
ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    maxs = 0
    for lists in itertools.permutations(strs):
        string = ''
        for j in lists:
            string+=j
        index = int(string)
        if index>maxs:
            print(lists)
            max = index
    ans.append(index)
for i in ans:
    print(i)
