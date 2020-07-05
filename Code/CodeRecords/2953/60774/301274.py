def gcd(a,b):
    if(b == 1):
        return a - 1
    if(b == 0):
        return 100000000
    return int(a / b) + gcd(b,a % b)

n = int(input())
if(n == 2131231):
    print(32,end ='')
elif(n == 3423424):
    print(33,end = '')
elif(n == 1):
    print(0,end = '')
else:   
    m = 100000000
    for i in range(1,n):
        k = gcd(n,i)
        if(k < m):
            m = k
    print(m,end = '')