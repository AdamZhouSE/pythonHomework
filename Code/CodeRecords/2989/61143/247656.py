str1 = input()
str2 = input()
str3 = input()
res = []
res.append(str1)
res.append(str2)
res.append(str3)
res.sort()
for i in range(len(res)):
    print(res[i])