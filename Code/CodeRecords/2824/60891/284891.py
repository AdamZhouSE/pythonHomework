n_t_c = [int(i) for i in input().split()]
n = n_t_c[0]
t = n_t_c[1]
c = n_t_c[2]
p = [int(i) for i in input().split()]
list_index = []
for i in range(n):
    if p[i] > t:
        list_index.append(i)
list_num = []
if len(list_index) == 0:
    ans = n - (c - 1)
else:
    list_num = [list_index[0] - 0]
    for i in range(len(list_index) - 1):
        list_num.append(list_index[i + 1] - list_index[i] - 1)
    ans = 0
    for i in list_num:
        if i >= c:
            ans += i - (c - 1)
    ans += (n - 1 - list_index[-1]) - (c - 1)
print(ans)
