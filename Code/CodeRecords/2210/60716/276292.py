ucnum = int(input())
ans = list()
for i in range(ucnum):
    str1 = input()
    str2 = input()
    anstr = str()
    lens = len(str1)
    for j in range(len(str1)-len(str2)):
        if str1[j]==str2[0]:
            check = True
            temp = j
            for t in range(1,len(str2)):
                if str2[t] not in list(str1[temp+1:]):
                    check = False
                    break
                else:
                    k = str1[temp+1:].index(str2[t])
                    temp = temp+1+k
            if check and temp-j<lens:
                anstr = str1[j:temp+1]
                lens = temp-j
    ans.append(anstr)
for i in ans:
    print(i)
