def transform(x):
    res = 0
    base = 0
    while x>0:
        digit = x&1
        if digit == 0:
            res+=2**base
        x = x>>1
        base+=1
    return res

t = int(input())
for i in range(t):
    print(transform(int(input())))