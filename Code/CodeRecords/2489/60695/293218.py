a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
lower = int(input())
upper = int(input())
c = 0

for i in range(1, len(a) + 1):
    for j in range(0, len(a) - i + 1):
        sum = 0
        for m in range(j, j+i):
            sum += a[m]
        if sum >= lower and sum <= upper:
            c += 1
print(c)
