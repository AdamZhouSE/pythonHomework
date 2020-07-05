str_input = input()
str_list = []
for ch in str_input:
    str_list.append(ch)
str_ope = eval(input())
for ch_list in str_ope:
    ch_list = [int(x) for x in ch_list]
    if ch_list[0] < ch_list[1] and ord(str_list[ch_list[0]]) > ord(str_list[ch_list[1]]):
        temp = str_list[ch_list[0]]
        str_list[ch_list[0]] = str_list[ch_list[1]]
        str_list[ch_list[1]] = temp
res = ''.join(str_list)
print(res)