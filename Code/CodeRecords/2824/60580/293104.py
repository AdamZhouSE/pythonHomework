a = input().split()
total = int(a[0])
max = int(a[1])
num = int(a[2])
b = input().split()
l = []
for i in b:
    l.append(int(i))
j = 0
result = 0
while j + num - 1 <= total - 1:
    k = j
    signal = 0
    while k <= j + num - 1:
        if l[k] > max:
            signal = 1
        k += 1
    if signal == 0:
        result += 1
    j += 1
print(result)
