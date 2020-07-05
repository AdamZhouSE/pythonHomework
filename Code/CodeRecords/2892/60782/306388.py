

line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]

a = [0] * 17
for i in range(n, m + 1):
    jjj = i
    while jjj > 0:
        a[jjj % 10] += 1
        jjj /= 10
for j in range(len(a) - 1):
    print(a[j], end=" ")
print(a[16])