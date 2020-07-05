a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
b = sorted(a)
b.reverse()
k = int(input())
capacity = b[0]
i = 0
sep = []
sum = 0
while True:
    while i < len(a):
        if sum + a[i] <= capacity:
            sum += a[i]
            i += 1
        else:
            sep.append(sum)
            sum = 0
    if i == len(a) and sum <= capacity:
        sep.append(sum)
    if len(sep) > k:
        sep = []
        i = 0
        sum = 0
        capacity += 1
    else:
        break
print(capacity)

