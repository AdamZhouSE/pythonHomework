def int2col(n):
    res = ""
    while n > 0:
        res = chr(ord('A')+(n-1)%26) + res
        n = int(n / 26)
    return res

if __name__ == "__main__":
    n = int(input())
    print(int2col(n))