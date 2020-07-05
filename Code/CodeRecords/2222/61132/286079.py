import functools

def proc(tmp,arg):
    return list(map(lambda x:[-int(x[0])] if len(x)==1 else \
            [-int(x[0]),arg] if x[0] else [-1,arg],tmp))

def evalu(inp,arg):
    s = inp.split('+')
    l = []
    if s[0][0] == '-':
        tmp = s[0]
        del s[0]
        tmp = list(map(lambda x: x.split(arg), tmp.split('-')[1:]))
        l += proc(tmp,arg)
    for i in s:
        tmp = i.split('-')
        ttmp=tmp.pop(0).split(arg)
        l.append([int(ttmp[0])] if len(ttmp)==1 else \
            [int(ttmp[0]),arg] if ttmp[0] else [1,arg])
        l += proc(tmp,arg)
    return l


def calcu(s):
    l1=[i for i in s if len(i)==2]
    l2=[i for i in s if len(i)==1]
    l1=functools.reduce(lambda a,b:[a[0]+b[0],a[1]],l1) if l1 else [0,'?']
    l2=functools.reduce(lambda a,b:[a[0]+b[0]],l2) if l2 else [0]
    if l1[0]==0:
        if l2[0]==0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return l1[1]+'='+str(int(-l2[0]/l1[0]))


s=input().split('=')
s1=evalu(s[0],'x')
s2=evalu(s[1],'x')
for i in s2:
    i[0]=-i[0]
print(calcu(s1+s2))