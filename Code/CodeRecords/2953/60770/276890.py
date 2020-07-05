def solve():
    n=int(input())
    res=float('inf')
    if n==1:
        print(0)
        return 
    m=int(n/2)
    for i in range(1,m+1):
        res=min(res,cnt((n,i)))
    print(res)

def cnt(pair):
    res=0
    while pair[0]!=pair[1]:
        if pair[0]>pair[1]:
            pair[0] -= pair[1]
        else:
            pair[1]-=pair[0]
        res+=1
    return res

if __name__ == '__main__':
    solve()