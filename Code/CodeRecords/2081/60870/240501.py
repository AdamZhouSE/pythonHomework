str_1 = input()
str_2 = input()
i = 0
count = 0
while i < len(str_1) - len(str_2) + 1:
    if str_1[i:i+len(str_2)] == str_2:
        count = count + 1
    i = i + 1
    while str_1[i] != str_2[0]:
        i = i + 1
print(count, end = '')