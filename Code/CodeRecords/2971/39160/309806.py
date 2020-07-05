import numpy as np

def find_repeat(source,elmt): 
    elmt_index=[]
    s_index = 0
    e_index = len(source)
    while s_index < e_index:
        try:
            temp = source.index(elmt,s_index,e_index)
            elmt_index.append(temp+1)
            s_index = temp + 1
        except ValueError:
            break
    return elmt_index

s = list(input())
ss = []
for i in s:
    ss.append(i)
ss.sort()

ans = []
temp = []

for i in range(len(ss)):
    temp.append(find_repeat(s, ss[i]))
    
for i in temp:
    le = len(i)
    for j in range(le):
        if not i[le - j - 1] in ans:
            ans.append(i[le - j - 1])
    
print(''.join(ans))