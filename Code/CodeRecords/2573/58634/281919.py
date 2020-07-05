# 2 2 4 8 16 512 256
# 1 1 2 3 4  9   8
# 1 2 3 4 5  6   7

def compute(n):
    if n%2 == 0:
        temp = n//2
        m = pow(3,temp-1)
        return int(pow(2,m))
    else:
        temp = (n-1)/2
        m = pow(2,temp)
        return int(pow(2,m))


t = int(input())
for i in range(t):
    print(compute(int(input())))
