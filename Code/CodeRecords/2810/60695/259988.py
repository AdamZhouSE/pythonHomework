m = input()
n = int(m)
sep = []
x = 10
while n > 0:
    sep.append(int(n % x))
    n = n - n % x
    x *= 10
result = []
for i in range(len(sep) - 1, -1, -1):
    if i == len(sep) - 1:
        while sep[i] > 0:
            result.append(10 ** i)
            sep[i] -= 10 ** i
        sep.remove(sep[i])
out = []
while len(result) > 0:
    a = 0
    mark = 0
    i = 0
    c = len(m)
    while i < len(result) and c > 0:
        if i == 0 and mark != result[i]:
            a += result[i]
            mark = result[i]
            result.remove(result[i])
            c -= 1
        else:
            if result[i] == mark:
                i += 1
            else:
                mark = result[i]
                a += mark
                c -= 1
                result.remove(result[i])
    out.append(a)
print(len(out))
print(out[0], end="")
for i in range(1, len(out)):
    print(" "+str(out[i]), end="")
print()