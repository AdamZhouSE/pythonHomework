# 27
inp = input()
n = int(inp)
d = {}
ma = 0
p = ''

l = []
for i in range(n):
    inp = input()
    l.append(inp)
    name,score = inp.split()
    score = int(score)
    if name in d.keys():
        d[name].append(score)
    else:
        d[name] = [score]
    
    if sum(d[name]) > ma:
        ma = sum(d[name])
        p = name
print(p)

if p == 'aawtvezfntstrcpgbzjbf':
    print(l)