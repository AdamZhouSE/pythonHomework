n = int(input())
while(n>0):
    m = int(input())
    ssum = 0
    for i in range (1,m+1):
        ssum += i*i
    print(ssum)
    n-=1