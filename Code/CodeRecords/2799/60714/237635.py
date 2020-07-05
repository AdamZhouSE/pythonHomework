from math import gcd

n = int(input())
money = [int(x) for x in input().split()]
flag = False
for i in range(0, n):
    for j in range(i, n):
        tempA = int(money[i] / gcd(money[i], money[j]))
        tempB = int(money[j] / gcd(money[i], money[j]))
        if (tempA % 2 is not 0 and tempA % 3 is not 0 and tempA is not 1) \
                or (tempB % 2 is not 0 and tempB % 3 is not 0 and tempB is not 1):
            flag = True
            break
if flag:
    print("No")
else:
    print("Yes")
