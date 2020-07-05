str_ope = input()
str_ope_list = []
for ch in str_ope:
    str_ope_list.append(ch)
str_pairs = input()
str_valid = ''
for ch in str_pairs:
    if '9' >= ch >= '0':
        str_valid = str_valid + ch
for i in range(0, len(str_valid) - 1, 2):
    index_1 = int(str_valid[i])
    index_2 = int(str_valid[i + 1])
    if str_ope_list[index_1] > str_ope_list[index_2]:
        temp = str_ope_list[index_1]
        str_ope_list[index_1] = str_ope_list[index_2]
        str_ope_list[index_2] = temp
print(''.join(str_ope_list))