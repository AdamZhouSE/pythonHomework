T = int(input())
for i in range(T):
    Str1 = list(input())
    Str2 =list(input())
    set1 = set(Str1)
    set2 = set(Str2)
    res = []
    for m in set1:
        if(m not in set2):
            res.append(m)
    for j in set2:
        if(j not in set1):
            res.append(j)
    res.sort()
    print("".join(res))
    print()