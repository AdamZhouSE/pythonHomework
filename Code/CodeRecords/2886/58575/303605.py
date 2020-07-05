n=int(input())
str1 = input().split(" ")
maxLength = 1
i = 1
while len(str1) != 0:
    if str1[i] in str1[0:i]:
        index = str1.index(str1[i])
        str1 = str1[0:index] + str1[index + 1:i] + str1[i + 1:]
        i -= 1
        continue
    else:
        maxLength = max(maxLength, i+1)
        i += 1
print(maxLength)