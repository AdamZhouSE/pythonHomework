# 17
from ast import literal_eval
inp = input() + input() + input() + input() + input() 
num = literal_eval(inp)
print(num)

l = [0,1,2]
def f(num,i,j,t,l):
    if num[i][j] > l:
        if i+1 in l:
            f(num,i+1,j,t+1)
        if i-1 in l:
            f(num,i-1,j,t+1)
        if j+1 in l:
            f(num,j+1,j,t+1)
        if j-1 in l:
            f(num,j-1,j,t+1)
    else:
        print(t)
        return
for i in range(3):
    for j in range(3):
        f(num,i,j,0)