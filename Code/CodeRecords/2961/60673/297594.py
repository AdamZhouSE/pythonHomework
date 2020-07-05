import collections

str1 = input()
res = []
p = ""
de = collections.deque([])
for i in range(len(str1)):
    de.append(str1[i])
temp=""
for i in range(len(str1)):
    temp+=de[i]
res.append(temp)
for i in range(len(str1)-1):
    de.rotate()
    temp = ""
    for i in range(len(str1)):
        temp += de[i]
    res.append(temp)
res.sort()
for i in range(len(str1)):
    p += res[i][-1]
print(p,end="")
