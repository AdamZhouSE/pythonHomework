n = int(input())
if n <= 2:
    print(format(1/n,'0,.5f'))
else:
    a = 0.5
    for i in range(3, n+1):
        a = 1/i + (i-2)/i * a
    print(format(a,'0,.5f'))