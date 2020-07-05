a = list(input())
for i in range(len(a)):
    a[i] = int(a[i])
product = 1
for i in range(len(a)):
    product = product * a[i]
s = 0
for i in range(len(a)):
    s = s + a[i]
print(product - s)