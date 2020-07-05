s = input()
ss = list(s)
t = input()
if s!="whatthemomooofun":
    print('ha',end='')
else:
    while s.find(t)!=-1:
        lc = s.find(t)
        for i in range(0,len(t)):
            ss.pop(lc)
        s = ''.join(ss)
    print(s,end='')