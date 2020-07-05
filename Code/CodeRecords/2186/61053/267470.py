if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(int( (n*(n+1)*(2*n+1))/12 + n*(n+1)/4))
    for res in ans:
        print(res)