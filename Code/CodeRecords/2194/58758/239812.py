import math


def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True


count = int(input())
ans = []
for i in range(0, count):
    line = input().split()
    left = int(line[0])
    right = int(line[1])
    seq = []
    for j in range(left, right+1):
        if isprime(j):
            seq.append(j)
    ans.append(seq)
for i in range(0, count):
    for j in ans[i]:
        if j == ans[i][len(ans[i])-1]:
            print(j)
        else:
            print(j, end=' ')
