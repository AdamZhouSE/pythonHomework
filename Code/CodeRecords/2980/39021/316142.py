def isIn(s1,s2):
    if s1 not in s2:
        print('no exist')
    

s = input()
opt = input().split()
res = s
if opt[0] =='D':
    isIn(opt[1],s)
    n = s.find(opt[1])
    res = s.replace(opt[1], '',1)
elif opt[0] == 'I':
    isIn(opt[1],s)
    n = s.rfind(opt[1])
    str = opt[2] + s[n:]
    res = s[:n]+str
elif opt[0] == 'R':
    isIn(opt[1],s)
    res = s.replace(opt[1], opt[2])
print(res)