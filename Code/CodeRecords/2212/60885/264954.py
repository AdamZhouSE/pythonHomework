def divisionsSum(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            # print('div %d'%i)
            count += i
    return count

def isNotEnough(n):
    return divisionsSum(n) < 2*n

def test():
    n = int(input())
    if isNotEnough(n):
        A.append(1)
    else:
        A.append(0)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)