a = input()
a = a[1: len(a)-1].split(",")
for i in range(len(a)):
    a[i] = int(a[i])
n = len(a)
a.sort()
i = 1
while True:
    if i in a:
        i += 1
    else:
        break
print(i)