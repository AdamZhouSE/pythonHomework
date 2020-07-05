def solve():
    n,c,m=map(int,input().split())
    flws=list(map(int,input().split()))
    cs=list(range(1,c+1))
    
    for _ in range(m):
        l,r=map(int,input().split())
        prt=flws[l-1:r]
        c=list(filter(lambda x:prt.count(x)>1,cs))
        print(len(c))
    
if __name__ == '__main__':
    solve()