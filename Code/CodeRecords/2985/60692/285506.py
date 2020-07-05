n = int(input())
str1 = ''
for i in range(1, n + 1):
    if i == 1:
        str1 = 'A'
    else:
        if i % 4 == 1:
            str1 = str1 + 'A' + str1
        elif i % 4 == 2:
            str1 = str1 + 'B' + str1
        elif i % 4 == 3:
            str1 = str1 + 'C' + str1
        else:
            str1 = str1 + 'D' + str1
print(str1)