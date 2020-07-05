num = int(input())
list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
len_dic = {}
for i in range(len(list_input)):
    sum_s = list_input[i]
    j = i
    if sum_s > num:
        continue
    elif sum_s == num:
        len_dic[1] = 1
        break
    while sum_s < num and j < len(list_input) - 1:
        j += 1
        sum_s = sum_s + list_input[j]
    if sum_s == num:
        len_dic[j - i + 1] = 1
if len(len_dic) == 0:
    print(0)
else:
    length = min(len_dic.keys())
    print(length)
