def solve():
    vers=[[]]

    def insert(v,x):
        o=vers[v][:]
        o.append(x)
        o.sort()
        vers.append(o)

    def delete(v,x):
        o=vers[v][:]
        if x in o:
            del o[o.index(x)]
            vers.append(o)

    def rankOf(v,x):
        o = vers[v][:]
        vers.append(o)
        return o.index(x)+1

    def numOf(v,rank):
        o = vers[v][:]
        vers.append(o)
        return o[rank-1]

    def before(v,x):
        o = vers[v][:]
        vers.append(o)
        o2=list(filter(lambda y:y<x,o))
        if not o2:
            return -2**31+1
        return o2[len(o2)-1]

    def after(v,x):
        o = vers[v][:]
        vers.append(o)
        o2=list(filter(lambda y:y>x,o))
        if not o2:
            return 2**31
        return o2[0]

    n=int(input())
    for i in range(n):
        v,op,x=map(int,input().split())
        if op==1:
            insert(v,x)
        elif op==2:
            delete(v,x)
        elif op==3:
            print(rankOf(v,x))
        elif op==4:
            print(numOf(v,x))
        elif op==5:
            print(before(v,x))
        elif op==6:
            print(after(v,x))

if __name__ == '__main__':
    solve()