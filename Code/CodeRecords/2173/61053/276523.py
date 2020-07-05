if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(n*(n+1)*(2*n+1)/6)
    for res in ans:
        print(int(res))