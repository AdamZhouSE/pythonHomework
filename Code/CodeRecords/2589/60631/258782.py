def lo(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lo(n-1)+lo(n-2)
t = int(input())
for i in range(t):
    n = int(input())
    print(lo(n))