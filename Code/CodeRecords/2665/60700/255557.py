def score(n, z):
    c = 0
    while z != 1:
        if n % z == 0:
            n -= 1
            z -= 1
            c += 1
        else:
            z -= 1
    return c


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in nums:
    num = i.split(' ')
    X = int(num[0])
    Y = int(num[1])
    Z = int(num[2])
    c = [score(X, Z), score(Y, Z)]
    print(str(c[0])+' '+str(c[1]))