
def compute(k, m,n,length):
    ''' if length>n:
        return 0
    '''
    if length == n:
        return 1
    res = 0
    for i in range(2 * k, m + 1):
        res += compute(i,m,n,length+1)
    return res

t = int(input())
for _ in range(t):
    m,n = map(int,input().split(" "))
    res = 0
    for i in range(1,m+1):
        res += compute(i,m,n,1)
    print(res)
