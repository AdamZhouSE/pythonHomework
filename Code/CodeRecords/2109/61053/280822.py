def calBit(n):
    ans = n
    while ans >= 10:
        ans = 0
        while n > 0:
            ans += n % 10
            n = int(n / 10)
        n = ans
    return ans

if __name__ == "__main__":
    n = int(input())
    print(calBit(n))