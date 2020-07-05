def isValid(n):
    n = n + 2
    for i in range(2, n):
        if n % i == 0:
            # print(i)
            print('No')
            return False
    print('Yes')
    return True


n = int(input())
for i in range(n):
    k = int(input())
    isValid(k)