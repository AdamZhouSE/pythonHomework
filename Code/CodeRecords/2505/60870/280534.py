str_input = input()
str_input = str_input[1:-1]
array = str_input.split(',')
dict_ch = {}
for ch in array:
    if ch in dict_ch.keys():
        dict_ch[ch] = dict_ch[ch] + 1
    else:
        dict_ch[ch] = 1
for ch in dict_ch.keys():
    if dict_ch[ch] > 1:
        print(ch)
        break