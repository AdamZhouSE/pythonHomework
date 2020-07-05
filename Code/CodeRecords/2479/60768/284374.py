oj = int(input())
for i in range(oj):
    str1 = list(set(input()))
    str2 = list(set(input()))
    for j in str2:
        if j in str1:
            str1.pop(str1.index(j))
        else:
            str1.append(j)
    str1.sort()
    print(''.join(str1))
    print()