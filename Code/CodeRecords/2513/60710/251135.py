def solve(m, p):
    l = []
    for k  in range(0,len(m)):
        for x in range(0,len(m[0])):
            l.append(m[k][x])
    l=sorted(l)
    #print(l)
    return l[p-1]
if __name__ == '__main__':
    x=int(input())
    m=[]
    c=0
    while c<x:
        n=input().split(",")
        n=list(map(int,n))
        m.append(n)
        c=c+1
    k=int(input())
    print(solve(m,k))