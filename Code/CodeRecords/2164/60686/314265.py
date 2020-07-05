nums = int(input())
str_list = []
for i in range(nums):
    str_input = input()
    str_list.append(str_input)
for i in range(nums):
    dict_ch = {}
    str_input = str_list[i]
    for ch in str_input:
        if ch not in dict_ch.keys():
            dict_ch[ch] = 1
        else:
            dict_ch[ch] = dict_ch[ch] + 1
    res = 0
    for ch in dict_ch.keys():
        res = res + dict_ch[ch] - 1
    print(res)