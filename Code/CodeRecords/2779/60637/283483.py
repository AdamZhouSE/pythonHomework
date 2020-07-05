def gcd(a,b):
    if(b>0):
        return (int)(gcd(b,a%b))
    else:
        return a
def lca(a,b):
    return (int)(a*b/gcd(a,b))
tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    arr=list(map(int,input().split(' ')))
    list.sort(arr)
    print(lca(arr[0],arr[n-1]))
