n = int(input())
data = list(map(int, input().split(' ')))
sign = [0 for i in range(n)]
big = max(data)
for i in range(5):
    big *= 2
    for j in range(len(data)):
        if sign[j] == 0:
            if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
                sign[j] = 1
for i in range(5):
    big *= 3
    for j in range(len(data)):
        if sign[j] == 0:
            if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
                sign[j] = 1
if all(sign):
    print('Yes')
else:
    print('No')
