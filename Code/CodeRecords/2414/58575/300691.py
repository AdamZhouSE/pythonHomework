def cal(n):
    if n==0:
        return 1
    sum=0
    i=n-1
    while i>=0:
        sum=sum+cal(i)
        i=i-1
    return sum

n=int(input())
successful=cal(n-1)
all=cal(n)
print("{:.5f}".format(successful/all))