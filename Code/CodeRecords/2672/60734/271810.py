def transform(x):
    lst = []
    while x>0:
        lst.append(x&1)
        x = x>>1
    for i in range(len(lst)+1,33):
        lst.append(0)
    res = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            res+=2**i
    return res
        
t = int(input())
for i in range(t):
    n = int(input())
    print(transform(n))