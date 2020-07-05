T = int(input())
for i in range(T):
    Str1 = input().split()
    Str2 =input().split()
    set1 = set(Str1)
    set2 = set(Str2)
    res = []
    for i in set1:
        if(i not in set2):
            res.append(i)
    for j in set2:
        if(j not in set1):
            res.append(j)
    res.sort()
    print("".join(res))