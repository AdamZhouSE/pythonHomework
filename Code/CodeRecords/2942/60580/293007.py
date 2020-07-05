a = input()
strList = input().split()
result = ""
strList.sort()
i = len(strList) - 1
while i >= 0:
    result = result + strList[i]
    i = i - 1
print(result, end="")