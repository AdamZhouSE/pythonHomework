def calBit(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = int(n / 10)
    return ans % 9

if __name__ == "__main__":
    n = int(input())
    print(calBit(n))