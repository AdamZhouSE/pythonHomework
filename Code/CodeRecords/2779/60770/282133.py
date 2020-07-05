def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

def solve():
    input()
    nums=list(map(int,input().split()))
    a,b=max(nums),min(nums)
    res=lcm(a,b)

    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()