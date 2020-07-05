if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(2*n**2+n)
    for res in ans:
        print(res)