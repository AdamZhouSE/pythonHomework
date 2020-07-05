def cal_sub_string(s):
    set0 = []
    for ii in range(len(s)):
        for jj in range(ii + 1, len(s) + 1):
            set0.append(s[ii:jj])
    return list(set0)


T = int(input())
for ttt in range(T):
    a_list = cal_sub_string(input())
    a_list = [list(i) for i in a_list]
    a_list = [(i.count('0'),i.count('1'),i.count('2'))for i in a_list]
    a_list = [i for i in a_list if i[0] == i[1] == i[2]]
    print(len(a_list))