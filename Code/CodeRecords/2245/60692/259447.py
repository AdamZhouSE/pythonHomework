num = int(input())
str_num = str(bin(num))[2:]
i = 0
j = i + 1
max_res = 0
while i < len(str_num) - 1 and j < len(str_num):
    if int(str_num[i]) == 1:
        j = i + 1
        while j < len(str_num) and int(str_num[j]) != 1:
            j += 1
        if j == len(str_num):
            break
        else:
            if j - i > max_res:
                max_res = j - i
            i = j
    i += 1

print(max_res)