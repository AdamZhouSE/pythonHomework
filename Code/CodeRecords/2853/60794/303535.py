aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
total = 0
odd = 0
for i in range(len(a)):
    total = total + a[i]
    if a[i] % 2 != 0:
        odd = odd + 1
if total % 2 == 0:
    print(len(a)-odd)
else:
    print(odd)