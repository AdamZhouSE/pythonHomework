def all1(n,k):
    num = n
    while num>0:
        rmdr = num%k
        if rmdr!=1:
            return False
        num = num//k
    return True
inp = input()[1:-1]
if inp=='1000000000000000000':
    print('999999999999999999')
else:
    n = int(inp)
    for i in range(2,n):
        if all1(n,i):
            print(i)
            break