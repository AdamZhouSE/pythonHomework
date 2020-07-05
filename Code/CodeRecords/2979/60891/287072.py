s = input().split()
len_list = []
for i in s:
    len_list.append(len(i))
max_l = max(len_list)
i = len_list.index(max_l)
print(s[i])