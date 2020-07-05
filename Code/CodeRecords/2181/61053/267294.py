if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(n**3+n)
    for res in ans:
        print(res)