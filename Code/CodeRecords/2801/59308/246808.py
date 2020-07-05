n = int(input())
a = [int(x) for x in input().split(' ')]

a.sort()
i = 0
j = len(a) - 1
b1 = a[j]
b2 = a[j-1]
b3 = a[j-2]
# b1 > b2 > b3
if b2 + b3 > b1:
    print('YES')
else:
    print('NO')




# 1 2 4