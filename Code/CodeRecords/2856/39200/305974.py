n = int(input())
x = []
h = []
for i in range(n):
    str1 = input().split()
    x.append(int(str1[0]))
    h.append(int(str1[1]))
count = 2
if n <= 2:
    print(n)
else:
    for i in range(1, n - 1):
        if x[i] - h[i] > x[i - 1]:
            count += 1
        elif x[i] + h[i] < x[i + 1]:
            x[i] += h[i]
            count += 1
print(count)
