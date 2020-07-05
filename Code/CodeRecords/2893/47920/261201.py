import math
def de(t):
    ti = []
    _min = int(min(t))
    for i in range(len(t)):
        if(_min != int(t[i])):
            ti.append(t[i])
    t = ti
    return t

inp = eval(input())
length = len(inp)
#print(length)
#print(inp)

for i in range(math.ceil(len(inp)/3)):
    if(inp.count(min(inp)) > 1):
        inp = de(inp)
        #print(inp)
    else:
        print(min(inp))