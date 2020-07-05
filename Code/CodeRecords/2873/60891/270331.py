n_m = [int(i) for i in input().split()]
n = n_m[0]
m = n_m[1]
n_list = [int(i) for i in input().split()]
m_list = [int(i) for i in input().split()]

res_list = []
for i in n_list:
    if m_list.__contains__(i):
        res_list.append(i)
res = ""
for i in res_list:
    res += (str(i) + " ")
print(res,end='')