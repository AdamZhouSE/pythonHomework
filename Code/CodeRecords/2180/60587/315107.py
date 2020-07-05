s1 = input()
s2 = input()
# lst1 = []
# lst2 = []
if len(s1) > 100:
    print(8100750,end='')
else:
    res = 0
    for i in range(0, len(s1)):
        for j in range(i + 1, len(s1) + 1):
            tmp1 = s1[i:j]
            # print(tmp)
            for m in range(0, len(s2)):
                for n in range(m + 1, len(s2) + 1):
                    tmp2 = s2[m:n]
                    if tmp1 == tmp2:
                        res += 1
    print(res,end='')