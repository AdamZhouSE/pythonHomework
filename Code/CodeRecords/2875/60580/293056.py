a = input()
l = input().split()
d = {}
i = 0
while i < len(l):
    d[i + 1] = int(l[i])
    i += 1
resultList = sorted(d.items(), key=lambda item: item[1])
result = ""
for val in resultList:
    result = result + str(val[0]) + " "
print(result.strip())