n_m = [int(i) for i in input().split()]
n = n_m[0]
m = n_m[1]
list_ans = []
for i in range(n):
    list_ans.append([])
for i in range(n):
    inp = input()
    for j in range(m):
        list_ans[i].append(inp[j])
a = [int(i) for i in input().split()]
ans = 0
for i in range(m):
    list_ea_q = []
    for j in range(n):
        list_ea_q.append(list_ans[j][i])
    set_q = set(list_ea_q)
    len_set_q = len(set_q)
    q_times = []
    for i in range(len_set_q):
        q_times.append(list_ea_q.count(set_q.pop()))
    ans += max(q_times) * a[i]
print(ans)