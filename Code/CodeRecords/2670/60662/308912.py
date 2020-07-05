t = int(input())
res = []
for i in range(t):
    n = int(input())
    st= bin(n).replace('0b','')
    length = len(st)
    res = 1
    for a in range(0,length):
        res = res*2
    print(res-n-1)