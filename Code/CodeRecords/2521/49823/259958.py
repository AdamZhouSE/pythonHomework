def z(l):
    length=len(l)
    m={}
    for i in l:
        if i not in m:
            m[i]=1
        else:
            m[i]+=1
    l=list(set(l))
    r=[]
    i=0
    while len(r)!=length:
        if m[l[i]]>0:
            r.append(l[i])
            m[l[i]]-=1
        i=(i+1)%len(l)
    print(r)
if __name__ == '__main__':
    z([int(i) for i in input()[1:-1].split(',')])
