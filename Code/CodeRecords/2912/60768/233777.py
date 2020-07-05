maxLen = 0
str = input()
for i in range(len(str)):
    result = ""
    for j in range(i, len(str)):
        if (str[j] not in result):
            result = result + str[j]
        else:
            break
    if (maxLen < len(result)):
        maxLen = len(result)

print(maxLen)