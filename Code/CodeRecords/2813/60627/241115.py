# 27
inp = input()
n = int(inp)
d = {}
ma = 0
p = ''
for i in range(n):
    inp = input()
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