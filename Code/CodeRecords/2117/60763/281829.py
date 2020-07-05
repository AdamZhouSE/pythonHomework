import math
n = int(input())
a = [1]*n
for i in range(2,n+1):
    # print(i)
    if i == 2:
        j = i
        while j <= n:
            a[j-1] = 0
            j += i
        # print(a)
    else:
        j = i
        while j <= n:
            if a[j - 1] == 0:
                a[j - 1] = 1
            else:
                a[j - 1] = 0
            j += i
        # print(a)
print(a.count(1))