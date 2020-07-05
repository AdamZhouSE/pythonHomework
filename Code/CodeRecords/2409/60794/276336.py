a = input().split(",")
for i in range(len(a)):
    a[i] = int(a[i])
odd = 0
even = 0
for x in a:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(min(odd, even))