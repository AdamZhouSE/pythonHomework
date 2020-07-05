aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
x = 0
for i in range(len(a)):
    x = 0
    for k in range(len(a)):
        if k == i:
            continue
        else:
            if a[k] % a[i] != 0:
                x = 1
                break
    if x == 0:
        print(a[i])
        x = 2
        break
if x != 2:
    print(-1)