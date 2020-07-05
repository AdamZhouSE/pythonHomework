s1 = input()
s2 = input()
lst1 = []
lst2 = []
for i in range(0, len(s1)):
    for j in range(i + 1, len(s1) + 1):
        tmp = s1[i:j]
        # print(tmp)
        lst1.append(tmp)
for i in range(0, len(s2)):
    for j in range(i + 1, len(s2) + 1):
        tmp = s2[i:j]
        lst2.append(tmp)
# print(lst1)
# print(lst2)
res = 0
for i in range(0, len(lst1)):
    for j in range(0, len(lst2)):
        if lst1[i] == lst2[j]:
            res += 1
print(res,end = '')
