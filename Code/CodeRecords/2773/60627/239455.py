# 17
from ast import literal_eval
inp = input() + input() + input() + input() + input() 
num = literal_eval(inp)

lis = [0,1,2]
ans = []
def f(num,i,j,t,l):
    global lis
    global ans
    if num[i][j] > l:
        l = num[i][j]
        if i+1 in lis:
            f(num,i+1,j,t+1,l)
        if i-1 in lis:
            f(num,i-1,j,t+1,l)
        if j+1 in lis:
            f(num,i,j+1,t+1,l)
        if j-1 in lis:
            f(num,i,j-1,t+1,l)
    else:
        ans.append(t)
        return
for i in range(3):
    for j in range(3):
        f(num,i,j,0,0)
print(max(ans))

if max(ans) == 3:
    print(num)