num = int(input())
for i in range(num):
    a = list(input())
    while int("".join(a)) >= 10:
        x = 0
        for j in range(len(a)):
            x = x + int(a[j])
        a = list(str(x))
    print(int("".join(a)))