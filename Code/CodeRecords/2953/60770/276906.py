def solve():
    n=int(input())
    res=float('inf')
    if n==1:
        print(0,end='')
        return
    m=int(n/2)
    for i in range(1,m+1):
        if gcd(n,i)!=1:
            continue
        res=min(res,cnt([n,i]))
    print(res,end='')

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def cnt(pair):
    res=0
    while pair[0]!=pair[1]:
        if pair[0]==1:
            res+=pair[1]-1
            break
        if pair[1]==1:
            res+=pair[0]-1
            break
        if pair[0]>pair[1]:
            res+=int(pair[0]/pair[1])
            pair[0] %= pair[1]
        else:
            res+=int(pair[1]/pair[0])
            pair[1] %= pair[0]
    return res

if __name__ == '__main__':
    solve()