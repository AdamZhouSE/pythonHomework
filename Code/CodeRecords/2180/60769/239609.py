str1 = input()
str2 = input()
count = 0
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        for k in range(len(str2) - j + i + 1):
            if str1[i:j] == str2[k:k + j - i]:
                count += 1
print(count,end="")