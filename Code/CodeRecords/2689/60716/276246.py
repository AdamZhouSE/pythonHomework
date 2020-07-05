ucnum = int(input())
ans = list()
for i in range(ucnum):
    strs = input().split()
    str1 = list(strs[0])
    str2 = list(strs[1])
    index = 0
    index+=len(str1)
    for j in str1:
        if j in str2:
            str2.remove(j)
    index+=len(str2)
    ans.append(index)
for i in ans:
    print(i)