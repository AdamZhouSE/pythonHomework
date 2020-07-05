a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        break
print(i)