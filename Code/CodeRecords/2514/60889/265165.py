str1 = input()
str2 = input()
i = 0
j = 0
while(j < len(str2)):
    if str1[i] == str2[j]:
        i = i + 1
    j = j + 1
    if i == len(str1):
        break
if i == len(str1):
    print(True)
else:
    print(False)