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
op = list(map(str, input().split()))

if op[0] == 'D':
    a = op[1]
    ind = (''.join(s).index(a))
    s.remove(s[ind])
    print(''.join(s))
elif op[0] == 'I':
    a1, a2 = op[1], op[2]
    count = find_repeat(s, a1)
    index = count[-1]
    s.insert(index - 1, a2)
    print(''.join(s))
elif op[0] == 'R':
    a1, a2 = op[1], op[2]
    if(str(s).find(a1) == -1):
        print('no exist')
    print(''.join(s).replace(a1, a2))