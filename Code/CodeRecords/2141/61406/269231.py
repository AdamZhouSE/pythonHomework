T = int(input())
for a in range(0,T):
    N = int(input())
    result =""
    for x in range(1,N+1):
        result=result+bin(x)[2:]+" "
    print(result)