a = input().split(",")
for i in range(len(a)):
    a[i] = int(a[i])
a.sort(reverse=True)
length = 0
for i in range(len(a) - 2):
    if a[i] < a[i + 1] + a[i + 2]:
        length = a[i] + a[i + 1] + a[i + 2]
        break
print(length)