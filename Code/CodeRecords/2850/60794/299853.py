aa = input()
a = input().split(" ")
res = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        zero = 0
        one = 0
        for k in range(i, j + 1):
            if a[k] == "0":
                zero = zero + 1
            else:
                one = one + 1
        t = zero - one
        if t > res:
            res = t
x = 0
for i in range(len(a)):
    if a[i] == "1":
        x = x + 1
print(x+res)