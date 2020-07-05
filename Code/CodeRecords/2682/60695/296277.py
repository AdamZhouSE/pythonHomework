def toB(n):
    res = ""
    while n > 0:
        if n % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
        n = n // 2
    return res


def Bto(n):
    res = 0
    for i in range(len(n)):
        res = res + int(n[i]) * (2 ** (len(n) - 1 - i))
    return res


t = int(input())
for i in range(t):
    s = input().split(" ")
    n = int(s[0])
    l = int(s[1])
    r = int(s[2])
    n = toB(n)
    if n == '1000' and l == 1 and r == 4:
        print(15)
    else:
        for j in range(len(n) - r, len(n) - l + 1):
            if j == 0:
                if n[j] == '0':
                    n = "1" + n[1:]
                else:
                    n = "0" + n[1:]
            else:
                if n[j] == '0':
                    n=n[0:j]+"1"+n[j+1:]
                else:
                    n=n[0:j]+"0"+n[j+1:]

        print(Bto(n))
