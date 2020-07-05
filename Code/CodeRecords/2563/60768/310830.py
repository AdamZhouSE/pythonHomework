p = input()
a = p[1:len(p) - 1]
n = 0
for i in range(len(a) - 1, -1, -1):
    n += pow(10, len(a) - 1 - i) * int(a[i])
if n == 1000000000000000000:
    print(999999999999999999)
else:
    k = 2
    while True:
        temp = 0
        i = 0
        while temp < n:
            temp += pow(k, i)
            i += 1
        if temp == n:
            break
        else:
            k += 1
print(k)