n = int(input())
while(n>0):
    m = int(input())
    n = m-1
    n = n*(n+1)
    m = m*(m+1)
    s = m*(m+1)/2 - n*(n+1)/2
    print(int(s))
    n-=1