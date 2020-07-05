# 20
n = int(input())
s = '['
for i in range(n):
    inp = input()
    s += ('[' + inp + '],')
s = s[:-1] + ']'
from ast import literal_eval
num = literal_eval(s)

l = []
def f(num,i,j,t,t_l):
    lis = range(len(num))
    global l 
    t += num[i][j]
    t_l.append(t)
    if i==len(num) - 1 and j==len(num) - 1:
        l.append(min(t_l))
        return
    if i+1 in lis:
        f(num,i+1,j,t,t_l[:])
    if j+1 in lis:
        f(num,i,j+1,t,t_l[:])
t_l = []
f(num,0,0,0,t_l)
print(-max(l) + 1)
