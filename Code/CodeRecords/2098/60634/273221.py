def tran(n):
    result = ""
    while n != 0:
        res = n % 26
        if res == 0:
            if n <= 26:
                n =0
            res = 26
        result = chr(ord('A') + res - 1) + result
        n = int(n / 26)
    return result


#main-----
n = int(input())
print(tran(n))