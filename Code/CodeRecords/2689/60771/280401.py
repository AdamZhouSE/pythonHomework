#26
T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    str1 = ori[0].lower()
    str2 = ori[1].lower()
    dup = []
    for c in str1:
        if c not in dup:
            dup.append(c)
    for c in str2:
        if c not in dup:
            dup.append(c)
    print(len(dup))
