# 效率还行 ？


def cal_sub_string(s):
    dict0 = {}
    for ii in range(len(s)):
        for jj in range(ii + 1, len(s) + 1):
            if s[ii:jj] in dict0:
                dict0[s[ii:jj]] += 1
            else:
                dict0[s[ii:jj]] = 1
    return dict0


s1 = input().strip()
s2 = input().strip()
dict1 = cal_sub_string(s1)
dict2 = cal_sub_string(s2)
num = 0
for i in dict1:
    if i in dict2:
        num += dict1[i] * dict2[i]
print(num, end='')