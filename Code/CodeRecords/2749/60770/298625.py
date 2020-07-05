def solve():
    n=int(input())
    fas=[0]+list(map(int,input().split()))
    chs=list(input())

    def strof(i):
        if fas[i]==0:
            return chs[i]
        return chs[i]+strof(fas[i]-1)

    ss=list(map(strof,range(n)))

    def cmp(a,b):
        if ss[a]!=ss[b]:
            return ss[a]>ss[b]
        if fas[a]==fas[b]:
            return a>b
        f1s=ss[fas[a]-1]
        f2s=ss[fas[b]-1]
        if f1s==f2s:
            return fas[a]>fas[b]
        return f1s>f2s

    res=list(range(n))
    for i in range(n-1,0,-1):
        for j in range(i):
            if cmp(res[j],res[j+1]):
                res[j],res[j+1]=res[j+1],res[j]
    res=list(map(lambda x:x+1,res))
    res=list(map(str,res))
    print(' '.join(res),end=' ')

if __name__ == '__main__':
    solve()