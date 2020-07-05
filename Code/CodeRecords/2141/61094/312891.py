T = int(input())
while(T>0):
    s = int(input())
    b2 = ''
    for i in range(1,s+1):
        b = str(bin(i))
        l = len(b)
        b1 = ''
        for i in range(2,l):
            b1 = b1+b[i]
        b2 = b2+b1+' '
    print(b2)
    T-=1