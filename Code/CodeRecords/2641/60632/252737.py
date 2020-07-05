s1 = list(input())
s2 = list(input())
find = False
for i in range(len(s2)):
    tmp = s1[:]
    for j in range(i, len(s2)):
        if s2[j] in tmp:
            tmp.remove(s2[j])
        else:
            break
    if len(tmp) == 0:
        find = True
        break
print(find)
