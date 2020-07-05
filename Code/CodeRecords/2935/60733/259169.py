l = list(input())
t = 0
ans = 0
q = list()
for i in range(len(l)):
    if l[i] =='Q':
        t = t + 1
    q.append(t)
for i in range(len(l)):
    if l[i] == 'A':
        ans = ans + q[i] * (t - q[i])
print(ans,end='')