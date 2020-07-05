def f(n):
    ans = 0
    for i in range(32):
        if n&1 == 1:
            ans += 1
        n = n >> 1
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(f(n))
    for res in ans:
        print(res)