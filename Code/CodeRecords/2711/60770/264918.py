def solve():
    src=input()[1:-1].replace('"','').split(',')
    total=len(src)
    disjointset=[-1 for i in range(total)]

    def isAlike(s1,s2):
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        dif1,dif2='',''
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if dif1=='':
                    dif1=s1[i]+s2[i]
                elif dif2=='':
                    dif2=s1[i]+s2[i]
                else:
                    return False
        if dif1[::-1]==dif2:
            return True
        else:
            return False

    def rootOf(index):
        nonlocal disjointset
        if disjointset[index]==-1:
            return index
        return rootOf(disjointset[index])

    def join(a,b):
        nonlocal disjointset
        roota=rootOf(a)
        rootb=rootOf(b)
        if roota==rootb:
            return
        disjointset[rootb]=roota

    for i in range(total):
        for j in range(i+1,total):
            if isAlike(src[i],src[j]):
                join(i,j)
    res=disjointset.count(-1)
    print(res)

if  __name__ == '__main__' :
    solve()