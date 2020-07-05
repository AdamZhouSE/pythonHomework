a = eval(input())
x = 0
for i in range(len(a)-1):
    while a[i] == a[i+1]:
        t = a[i+1]
        for j in range(i+1, len(a)-1):
            a[j] = a[j + 1]
        a[len(a)-1] = t
        x = x + 1
        if x == 1000000:
            x = -1
            break
if x == -1:
    list.reverse(a)
    for i in range(len(a) - 1):
        while a[i] == a[i + 1]:
            t = a[i + 1]
            for j in range(i + 1, len(a) - 1):
                a[j] = a[j + 1]
            a[len(a) - 1] = t
            x = x + 1
            if x == 1000000:
                x = -1
                break
print(a)