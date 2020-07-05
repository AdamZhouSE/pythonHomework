def iii():
    s=input()
    row=-1
    for x in s:
        if x=='[':
            row+=1;
    s=s.replace('[','')
    s=s.replace(']','')
    s=s.replace(',',' ')
    l=s.split()
    l= list(map(int, l))

    gap=int(len(l)/row)

    d1=[]
    for i in range(0, len(l), gap):
        dd=[]
        for j in range(gap):
            dd.append(l[i+j])
        d1.append(dd)

    return d1

def smallestStringWithSwaps(s, pairs):
    p = {i:i for i in range(len(s))}

    def f(x):
        if x != p[x]:
            p[x] = f(p[x])
        return p[x]
    
    for i, j in pairs:
        p[f(j)] = f(i)      
    d = collections.defaultdict(list)
    for i, j in enumerate(map(f, p)):
        d[j].append(i)
    ans = list(s)
    for q in d.values():
        t = sorted(ans[i] for i in q)   
        for i, c in zip(sorted(q), t):
            ans[i] = c
    return ''.join(ans)
s=input()
d=iii()
print(smallestStringWithSwaps(s,d))