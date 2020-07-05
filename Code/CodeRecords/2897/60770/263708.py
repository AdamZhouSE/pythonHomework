def solve():
    srcs=input()[1:-1].replace('"','').split(',')
    res=0
    for i in range(len(srcs)):
        for j in range(i+1,len(srcs)):
            if isOK(srcs[i],srcs[j]):
                current=len(srcs[i])*len(srcs[j])
                if current>res:
                    res=current
    print(res)

def isOK(s1,s2):
    set1=set(s1)
    set2=set(s2)
    return set1.isdisjoint(set2)

if  __name__ == '__main__' :
    solve()