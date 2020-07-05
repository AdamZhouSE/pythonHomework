T = int(input())
for a in range(0,T):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    source = input().split(' ')
    delta = abs(int(source[0])-k)
    num = source[0]
    for i in source:
        if abs(int(i)-k)<=delta:
            delta = abs(int(i)-k)
            num = i
    print(num)
    
            