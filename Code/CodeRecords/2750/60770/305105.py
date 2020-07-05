from collections import defaultdict

def solve():
    n=int(input())
    edges=eval(input())
    
    if n==1:
        return [0]
    
    e=defaultdict(set)
    for i,j in edges:
        e[i]|={j}
        e[j]|={i}
    q={_ for _ in e if len(e[_])==1}
    while n>2:
        t=set()
        for i in q:
            j=e[i].pop()
            e[j]-={i}
            if len(e[j])==1:
                t|={j}
            n-=1
        q=t
    return list(q)

if __name__ == '__main__':
    print(solve())