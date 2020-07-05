t = int(input())
while t:
    n = int(input())
    ret = ''
    for i in range(1, n+1):
        temp = str(bin(i))[2:]
        ret = ret + temp + ' '
    print(ret)
    t -=1 
    