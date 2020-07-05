str_1 = input()
str_2 = input()
res = ""
for i in range(len(str_1)):
    if str_1[i] in str_2:
        tmp = str_2.split(str_1[i])
        res = res + str_1[i]*(len(tmp) - 1)
        str_2 = ''.join(tmp)
print(res + str_2)