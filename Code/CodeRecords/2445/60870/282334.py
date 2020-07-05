str_input = input()
str_list = str_input.split(',')
s_str = str_list[0]
t_str = str_list[1]
s_str = s_str[s_str.index('\"') + 1:-1]
t_str = t_str[t_str.index('\"') + 1:-1]
s_dict = {}
t_dict = {}
for ch in s_str:
    if ch not in s_dict.keys():
        s_dict[ch] = 1
    else:
        s_dict[ch] = s_dict[ch] + 1
for ch in t_str:
    if ch not in t_dict.keys():
        t_dict[ch] = 1
    else:
        t_dict[ch] = t_dict[ch] + 1
if s_dict == t_dict:
    print('true')
else:
    print('false')