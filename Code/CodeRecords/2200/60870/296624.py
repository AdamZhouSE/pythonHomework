str_tf = input()
str_gb = input()
k = int(input())
cnt = 0
dict_res = {}
for i in range(0, len(str_tf)):
    for j in range(i + 1, len(str_tf) + 1):
        str_check = str_gb[i:j]
        str_sub = str_tf[i:j]
        k_cnt = 0
        for ch in str_check:
            if ch == '1':
                k_cnt = k_cnt + 1
        if k_cnt <= k:
            if str_sub not in dict_res.keys():
                dict_res[str_sub] = 1
            else:
                pass
cnt = len(dict_res)
print(cnt)