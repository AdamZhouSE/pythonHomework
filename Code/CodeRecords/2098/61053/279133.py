def int2col(n):
    res = ""
    n = n - 1
    do:
        res = chr(ord('A')+(n-1)%25) + res
        n = int(n / 26)
    while n > 0
    return res

if __name__ == "__main__":
    n = int(input())
    print(int2col(n))