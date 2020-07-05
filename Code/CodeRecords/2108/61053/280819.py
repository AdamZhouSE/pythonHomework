def count_1(n):
    count = 0
    while n > 0:
        if n % 10 == 1:
            count += 1
        n = int(n / 10)
    return count

if __name__ == "__main__":
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        ans += count_1(i)
    print(ans)