import math

a = input().split("[")
b = a[1]
c = b.split("]")
num = list(map(int, c[0].split(",")))
k = int(c[1][6])
t = int(c[1][-1])
for i in range(len(num)):
    for j in range(len(num)):
        if (i != j and (abs(num[i] - num[j]) <= t and abs(i - j) <= k)):
            answer = 'true'
print(answer)