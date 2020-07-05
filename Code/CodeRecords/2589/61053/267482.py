def lukas(k):
    if k == 0:
        return 2
    if k == 1:
        return 1
    L0 = 2
    L1 = 1
    L = 0
    for i in range(k-1):
        L = L0 + L1
        L0 = L1
        L1 = L
    return L

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(lukas(n))
    for res in ans:
        print(res)