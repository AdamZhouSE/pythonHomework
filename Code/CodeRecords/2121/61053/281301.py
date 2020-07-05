def cal(n):
    if n == 1:
        return 10
    if n == 2:
        return 91
    ans = 91
    last = 81
    for i in range(2,n):
        last = (10-i) * last
        ans += last
    return ans

if __name__ == "__main__":
    n = int(input())
    print(cal(n))