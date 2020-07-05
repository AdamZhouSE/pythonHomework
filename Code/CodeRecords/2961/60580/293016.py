a = input()
length = int(len(a))
i = 0
strList = []
while i < len(a):
    strList.append(a[i:length] + a[0:i])
    i = i + 1
strList.sort()
result = ""
for temp in strList:
    result = result + temp[length - 1]
print(result, end="")