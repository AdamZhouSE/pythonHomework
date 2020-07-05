

test = int(input())
for i in range(test):
    n = int(input())
    all = []
    root = int(n**0.5)
    for j in range(1,root):
        if n % j == 0:
            all.append(j)
            all.append(n / j)
    if root**2 == n:
        all.append(root)
    else:
        if n % root == 0:
            all.append(root)
            all.append(n / root)
    sum1 = 0
    for x in all:
        sum1 += x
    if sum1 < 2*n:
        print(1)
    else:
        print(0)