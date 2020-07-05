def sum(m , n):
    if m>n:
        return 0
    else:
        return 1+sum(2*m,n)+sum(2*m+1,n)


while True:
    inner = [int(i)for i in input().split()]
    m, n = inner[0], inner[1]
    if m==n==0:
        break
    print(sum(m, n))