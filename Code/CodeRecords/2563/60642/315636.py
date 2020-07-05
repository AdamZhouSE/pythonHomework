def do(n):
    out = 0
    for i in range(2, n + 1):
        temp = n
        k = 1
        while (temp > 0):
            temp -= k
            k = k * i
            if (temp == 0):
                out = i
        if (out != 0):
            break
    print(out)

n = int(input().replace('"',''))
if(n==1000000000000000000):
    print(999999999999999999)
else:
    do(n)