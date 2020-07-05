t = int(input())

for i in range(t):
    n = int(input())
    if(n%2 == 0):
        e = int(n/2)-1
        re = pow(2,pow(3,e))
    else:
        e = int(n/2)
        re = pow(2,pow(2,e))
    print(re)