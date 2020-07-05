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
def f(num,i,j,t):
    lis = range(len(num))
    global l 
    t += num[i][j]
    
    if i==len(num) - 1 and j==len(num) - 1:
        l.append(t + 1)
        return
    if i+1 in lis:
        f(num,i+1,j,t)
    if j+1 in lis:
        f(num,i,j+1,t)
f(num,0,0,0)
print(l)
print(num)