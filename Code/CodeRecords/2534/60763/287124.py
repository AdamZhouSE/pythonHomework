s = eval(input())
# print(s[1])
a = []
for i in s:
    for j in i:
        a.append(j)
print(sorted(a))