a = input()
a = a[1: len(a)-1].split(",")
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
l = ml = 1

for n in range(1, len(a)):
    if a[n] == a[n-1]+1:
        l += 1
    else:
        ml = max(ml, l)
        l = 1
print(ml)
