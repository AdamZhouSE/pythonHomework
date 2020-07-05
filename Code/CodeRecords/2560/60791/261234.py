from collections import Counter
def solve(n,a,m):
    dic = dict(Counter(a))
    val = []
    for key,value in dic.items():
        val.append(value)
    val = sorted(val)
    count = 0
    for item in val:
        if(m>=item):
            m-=item
            count+=1
        else:
            break
    return len(val)-count

T = int(input())
x = 0
while(x<T):
    x+=1
    N = int(input())
    a = [int(i) for i in input().split()]
    m = int(input())
    print(solve(N,a,m))