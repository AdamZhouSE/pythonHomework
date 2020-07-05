list1 = []
res = []
s = input()
for i in range(0, len(s)):
    list1.append([s[i:], i + 1])
list1.sort()
for i in list1:
    res.append(str(i[1]))
print(" ".join(res))